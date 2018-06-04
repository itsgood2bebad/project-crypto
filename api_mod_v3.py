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
        for val_2 in self.data[1]['data']['quotes']['USD'].values():
            btc_change.append(val_2)
        btc_change.append(self.data[1]['metadata']['timestamp'])
        with open(self.path[1],'a') as f:
            dict_data = csv.writer(f)
            dict_data.writerow(btc_change)
            print('nouvelle entrées dans les csv')
        return (eth_change[:6]+btc_change[:6])

    def run(self):

        if os.path.exists(self.path[0]):
            self.addrows()
        else:
            self.create_col(),
            self.addrows()

    def market_val():

        df = pd.read_csv('csv_test.csv')
        return(((df.market_cap).mean()),(max(df.market_cap)))

    def last_row(path):

        df = pd.read_csv(path)
        return (df[-1:].values.tolist())[0][:6]


def registre_s(obj):
        with open('a', 'wb') as f:
            save = pickle.Pickler(f)
            save.dump(obj)

def registre_l():
        with open('a','rb') as f:
            load = pickle.load(f)
            return load
