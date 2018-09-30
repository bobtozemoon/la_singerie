# Exemple d'un script python qui affiche le cours des coins sur kucoin

import urllib2
import json
import cookielib


# Creation de la classe crypto.

class crypto:
    def __init__(self,symbol):
        self.symbol = symbol.upper()
    def get_price(self):  
        url = "https://api.kucoin.com/v1/"+self.symbol+"-BTC/open/tick"
        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
        req = urllib2.Request(url, headers=hdr)
        reponse = urllib2.urlopen(req)
        data = json.load(reponse)
        print data["data"]["lastDealPrice"]
 
# On appelle la classe crypto qui va afficher la valeur du coin voulu

car_vertical = crypto("CV")
car_vertical.get_price()

te_food = crypto("TFD")
te_food.get_price()
