from flask import Flask
app = Flask(__name__)
import os
import requests
import json
import jsonpickle

# python3 -m flask run
# import simfin as sf
# from simfin.names import *

# sf.set_api_key('a3dde4ef-6674-4b65-84a3-a9ff2e7c81f2')
# sf.set_data_dir(os.getcwd()+'/simfin_data/')
# df = sf.load_income(variant='annual', market='us')

@app.route("/")
def home():
    return "Hello World! I'm using Flask."

@app.route("/stockdata")
def stockdata():
    # print(df.loc['MSFT'])
    # f = open("stockdata.json", "wb")
    # x = requests.get('http://api.marketstack.com/v1/eod?access_key=f7d07c1e14f18faaa3eb88fa3e75f99d&symbols=MSFT,AAPL,GOOGL,AMZN,BABA,FB,V,JPM,TSM,INTC,KO')
    # f.write(x.content)
      
    # Opening JSON file
    f = open('stockdata.json')
    
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
    
    # Iterating through the json
    # list
    # for i in data['data']:
    #     print(i)
    #     res = i
    # res = data['data']
    companies = ["MSFT", "V", "AAPL", "GOOGL", "JPM", "KO", "AMZN", "TSM", "INTC", "BABA"]
    mydic = {}
    count = 0
    for symbol in companies:
        res = list(filter(lambda x:x["symbol"]==symbol,data['data']))
    # result = [x for x in data if x["symbol"]=="MSFT"]
        mydic[companies[count]] = res[0]
        count = count +1

    print(mydic)
    # Closing file
    f.close()
    return jsonpickle.encode(mydic)
    # return  jsonpickle.encode(y)