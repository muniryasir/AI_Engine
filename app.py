from flask import Flask
app = Flask(__name__)
import os
import requests
import json
import jsonpickle
import statistics
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
from flask import request as frequests
# python3 -m flask run
# import simfin as sf
# from simfin.names import *

# sf.set_api_key('a3dde4ef-6674-4b65-84a3-a9ff2e7c81f2')
# sf.set_data_dir(os.getcwd()+'/simfin_data/')
# df = sf.load_income(variant='annual', market='us')

@app.route("/")
@cross_origin()
def home():
    return "Hello World! I'm using Flask2."

@app.route("/stockdata")
@cross_origin()
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
    companiesNames = ["Microsoft Corporation", "Visa Inc", "Apple Inc", "Alphabet Inc", "JPMorgan Chase", "Coca-Cola", "Amazon.com Inc", "Taiwan Semiconductor Manufacturing", "Intel Corp", "Alibaba Group"]
    mydic = {}
    count = 0
    for symbol in companies:
        res = list(filter(lambda x:x["symbol"]==symbol,data['data']))
    # result = [x for x in data if x["symbol"]=="MSFT"]
        
        datalist = dict()
        countD = 0
        for dataL in res:
            datadict = {}
            tempdic = dict(dataL)
            print(tempdic)
            datadict["closeprice"] = tempdic['close']
            datadict["date"] = tempdic["date"]
            # datadict["name"] = tempdic["name"]
            # res1 = dict(data)
            datalist[countD] = datadict  
            countD = countD + 1  
        datalist['name'] = companiesNames[count]    
        mydic[symbol]= datalist
        # mydic["name"]= companiesNames[count]
        # mydic[companies[count]] = res1
        count = count +1

    print(mydic)
    # Closing file
    f.close()
    return jsonpickle.encode(mydic)
    # return  jsonpickle.encode(y)

@app.route("/prediction")
@cross_origin()
def stockprediction():
    symbol = frequests.args.get('symbol')
    # print(symbol)
    f = open('stockdata.json')
    data = json.load(f)
    res = list(filter(lambda x:x["symbol"]==symbol,data['data']))
    pricePerCycle = list()
    for item in res:
        pricePerCycle.append(item["close"])
    # print(pricePerCycle)
    sampleList, trendList = createTrendList(pricePerCycle)
    createPredictionList(sampleList, trendList)
    return "working "+symbol

def createTrendList(sampleList):
    trendList = list()
   
    # foo = somevalue
    prevItem = nextItem = None
    l = len(sampleList)
    for index, item in enumerate(sampleList):
        if index > 0:
            prevItem = sampleList[index - 1]
        if index < (l - 1):
            next_ = sampleList[index + 1]
        if index == 0:
            prevItem = 0
        currentItem = sampleList[index]
        trendList.append(prevItem-currentItem)
    
    # print(trendList)
    return sampleList, trendList

def createPredictionList(sampleList, trendList):
    # print(sampleList, trendList)
    mean = statistics.mean(sampleList)
    stdDeviation = statistics.stdev(sampleList)
    print("mean :",mean)
    print("stddev :",stdDeviation)
    # predictedList
    return 0