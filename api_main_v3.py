from api_mod_v3 import n_current, registre_s, registre_l, recup_val

x = n_current(('https://api.coinmarketcap.com/v2/ticker/1027?convert=EUR.json','https://api.coinmarketcap.com/v2/ticker/1?convert=EUR.json'),('newstest3.csv','newstest4.csv'))
m_stat = x.market_val()
sc = x.run()
l_sc = (registre_l()).run()
fin = recup_val(sc,l_sc, m_stat)
fin.print_info()
