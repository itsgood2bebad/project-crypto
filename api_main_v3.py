from api_mod_v3 import n_current, registre_s, registre_l, recup_val

x = n_current(('https://api.coinmarketcap.com/v2/ticker/1027?convert=EUR.json','https://api.coinmarketcap.com/v2/ticker/1?convert=EUR.json'),('newstest4.csv','newstest3.csv'))
l_sc = registre_l()
sc = x.run()
registre_s(sc)
m_stat = x.market_val()
fin = recup_val(sc, l_sc, m_stat)
fin.print_info()
