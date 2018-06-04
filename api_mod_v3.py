import pandas as pd
import requests
import json
import urllib.request as urllib
import csv
import os
import pickle

class n_current:

    def __init__(self,url,path):
        self.url = url
        self.path = path
        self.data = self.read()
        self.save = 0
        self.load = 0

    def __getstate__(self):
        a = self.__dict__
        a["save"]+=1
        return a

    def __setstate__(self, attr):
        attr["load"]+=1
        self.__dict__ = attr

    def __repr__(self):
        return str(self.__dict__)

    def read(self):

        json_obj1 = urllib.urlopen(self.url[0])
        data1 = json.load(json_obj1)
        json_obj2 = urllib.urlopen(self.url[1])
        data2 = json.load(json_obj2)
        print('read ok')
        return (data1,data2)

    def create_col(self):

        fieldn = []
        for val in self.data[0]['data']['quotes']['USD']:
            fieldn.append(val)
        fieldn.append('timestamp')
        with open(self.path[0],'w') as f, open(self.path[1],'w') as g:
            dict_data = csv.DictWriter(f,fieldnames=fieldn)
            dict_data.writeheader()
            dict_data = csv.DictWriter(g,fieldnames=fieldn)
            dict_data.writeheader()
            print('- csv créés ')

    def addrows(self):

        eth_change = []
        btc_change = []
        for val in self.data[0]['data']['quotes']['USD'].values():
            eth_change.append(val)
        eth_change.append(self.data[0]['metadata']['timestamp'])
        with open(self.path[0],'a') as f:
            dict_data = csv.writer(f)
            dict_data.writerow(eth_change)
        print(eth_change)
        for val_2 in self.data[1]['data']['quotes']['USD'].values():
            btc_change.append(val_2)
        btc_change.append(self.data[1]['metadata']['timestamp'])
        with open(self.path[1],'a') as f:
            dict_data = csv.writer(f)
            dict_data.writerow(btc_change)
        print(btc_change)
        return (eth_change[:6]+btc_change[:6])

    def run(self):

        if os.path.exists(self.path[0]):
            val = self.addrows()
        else:
            self.create_col(),
            val = self.addrows()
        return val

    def market_val(self):

        df = pd.read_csv('newstest3.csv')
        return(((df.market_cap).mean()),(max(df.market_cap)))

    def last_row(path):

        df = pd.read_csv(path)
        return (df[-1:].values.tolist())[0][:6]


class recup_val:


    def __init__(self, scan, l_scan, mark_stat):

        self.price = (scan[0],scan[6],l_scan[0],l_scan[6])
        self.market = (scan[2],scan[8],l_scan[2],l_scan[8])
        self.hour = (scan[3],scan[9],l_scan[3],l_scan[9])
        self.day = (scan[4],scan[10],l_scan[4],l_scan[10])
        self.week = (scan[5],scan[11],l_scan[5],l_scan[11])
        self.mark = (mark_stat[0],mark_stat[1])
        self.eth_note = 0
        self.etc_evo = (l_scan[2] - scan[2])#evolution market depuis dernier scan
        self.etc_percent = round(((scan[0]/(l_scan[0]/100))-100),2)

    def crypt_eval(self):


        if self.hour[1] > 0:
            self.eth_note =+ 4
        if self.hour[1] < 0:
            self.eth_note =-4
        if self.day[1] > 0:
            self.eth_note =+ 2
        if self.day[1] < 0:
            self.eth_note =- 2
        if self.market[0] > self.mark[1]:
            self.eth_note =+ 6
        if self.market[0] > self.mark[0]:
            self.eth_note =+ 2
        if self.market[0] < self.mark[0]:
            self.eth_note =+ 3

    def print_info(self):
        print('\n'*2)
        print("- Le cap du marché jounalier de l ether est a :",self.market[0])
        print("- Le cap du marché jounalier du btc est a :",self.market[1])
        print('_'*100,'\n'*2)
        print("- L'évolution de l ether est de ",self.hour[0],"%  pour cette dernière heure")
        print("- L'évolution du bitcoin est de ",self.hour[1],"%  pour cette dernière heure")
        print('_'*100,'\n'*4)
        print("- La note actuel de l ether est de :",self.eth_note)
        print("- Le marché a evoluée de {} depuis la dérnière séquence ".format(self.etc_evo))
        print("- Le prix de l'ether a evoluée de {} depuis la dérnière séquence ".format(round((self.price[0] - self.price[2]),2)))
        print("- L'ether a evoluée de {}% depuis la dérnière séquence ".format(self.etc_percent))


def registre_s(obj):
        with open('a', 'wb') as f:
            save = pickle.Pickler(f)
            save.dump(obj)

def registre_l():
        with open('a','rb') as f:
            load = pickle.load(f)
            return load
