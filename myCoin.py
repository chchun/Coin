import json
import urllib.request
from urllib.request import Request, urlopen

class Exchange:
    dic_coin = {"BTC":0, "ETH":0, "XRP":0}

    def __init__(self):
        print ("init")

    def getTicker(self,type):
        if type in self.dic_coin:
            return  self.dic_coin[type]
        else:
            return -1

class Coinone(Exchange):
    URL = 'https://api.coinone.co.kr/ticker/?currency=all'

    def __init__(self):
        print ("Coinone")
        urlTicker = urllib.request.urlopen(self.URL)
        readTicker = urlTicker.read()
        jsonTicker = json.loads(readTicker)
        self.dic_coin['BTC'] = int(jsonTicker['etc']['last'])
        self.dic_coin['ETH'] = int(jsonTicker['eth']['last'])
        self.dic_coin['XRP'] = int(jsonTicker['xrp']['last'])

class Bithumb(Exchange):
    URL = 'https://api.bithumb.com/public/ticker/all'

    def __init__(self):
        print ("Bithumb")
        urlTicker = urllib.request.urlopen(self.URL)
        readTicker = urlTicker.read()
        jsonTicker = json.loads(readTicker)
        self.dic_coin['BTC'] = int(jsonTicker['data']['BTC']['closing_price'])
        self.dic_coin['ETH'] = int(jsonTicker['data']['ETH']['closing_price'])
        self.dic_coin['XRP'] = int(jsonTicker['data']['XRP']['closing_price'])


c = Coinone()
print ("코인원 정보")
print ("BTC: " + str(c.getTicker("BTC")))
print ("ETH: " + str(c.getTicker("ETH")))
print ("XRP: " + str(c.getTicker("XRP")))

b = Bithumb()
print ("빗썸 정보")
print ("BTC: " + str(b.getTicker("BTC")))
print ("ETH: " + str(b.getTicker("ETH")))
print ("XRP: " + str(b.getTicker("XRP")))