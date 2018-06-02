import pandas as pd
import time
import matplotlib.pyplot as plt
import datetime
import numpy as np
btc =pd.read_html("https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20180227&end="+time.strftime("%Y%m%d"))[0]
eth =pd.read_html("https://coinmarketcap.com/currencies/ethereum/historical-data/?start=20180227&end="+time.strftime("%Y%m%d"))[0]

btc = btc.assign(Date=pd.to_datetime(btc['Date']))
eth = eth.assign(Date=pd.to_datetime(eth['Date']))
btc['Volume'] = btc['Volume'].astype('int64')
eth['Volume'] = eth['Volume'].astype('int64')


fig, (ax1, ax2) = plt.subplots(2,1, gridspec_kw = {'height_ratios':[3, 1]})
ax1.set_ylabel(' Price btc',fontsize=10)
ax2.set_ylabel('Volume btc',fontsize=10)
ax2.set_yticks([int('%d000000000'%i) for i in range(10)])
ax2.set_yticklabels(range(10))
ax1.set_xticklabels('')
ax1.set_title('Valeur du btc')
ax1.plot(btc['Date'].astype(datetime.datetime),btc['Open*'])
ax2.bar(btc['Date'].astype(datetime.datetime).values, btc['Volume'].values)
plt.show()

fig, (ax1, ax2) = plt.subplots(2,1, gridspec_kw = {'height_ratios':[3, 1]})
ax1.set_ylabel(' Prix eth',fontsize=10)
ax2.set_ylabel('Volume eth',fontsize=10)
ax2.set_yticks([int('%d000000000'%i) for i in range(10)])
ax2.set_yticklabels(range(10))
ax1.set_title('Valeur de ETH')
ax1.set_xticklabels('')
ax1.plot(eth['Date'].astype(datetime.datetime),eth['Open*'])
ax2.bar(eth['Date'].astype(datetime.datetime).values,eth['Volume'].values)
plt.show()

fig, (ax1, ax2) = plt.subplots(2,1, gridspec_kw = {'height_ratios':[3, 1]})
ax1.set_ylabel(' Prix btc',fontsize=10)
ax2.set_ylabel('prix eth',fontsize=10)
ax2.set_yticks([int('%d000000000'%i) for i in range(10)])
ax2.set_yticklabels(range(10))
ax1.set_xticklabels('')
ax1.plot(btc['Date'].astype(datetime.datetime),btc['Open*'])
ax2.plot(eth['Date'].astype(datetime.datetime).values, eth['Open*'])
plt.show()

split_date = '2018-04-01'


fig, (ax1, ax2) = plt.subplots(2,1)
ax1.set_xticklabels('')

ax1.plot(btc[btc['Date']>= split_date]['Date'].astype(datetime.datetime),
         btc[btc['Date']>= split_date]['Close**'].values, label='Actuelle')
ax1.plot(btc[btc['Date']>= split_date]['Date'].astype(datetime.datetime),
          btc[btc['Date']>= datetime.datetime.strptime(split_date, '%Y-%m-%d') - 
                      datetime.timedelta(days=1)]['Close**'][1:].values, label='Prediction')
ax1.set_ylabel('Prix du bitcoin',fontsize=12)
ax1.legend(bbox_to_anchor=(0.1, 1), loc=2, borderaxespad=0., prop={'size': 14})
ax1.set_title('Prévision en n+1')
ax2.set_ylabel(' Prix ethereum',fontsize=12)
ax2.plot(eth[eth['Date']>= split_date]['Date'].astype(datetime.datetime),
         eth[eth['Date']>= split_date]['Close**'].values, label='Actuelle')
ax2.plot(eth[eth['Date']>= split_date]['Date'].astype(datetime.datetime),
          eth[eth['Date']>= datetime.datetime.strptime(split_date, '%Y-%m-%d') - 
                      datetime.timedelta(days=1)]['Close**'][1:].values, label='Prediction')
plt.show()






