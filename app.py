from flask import Flask
app = Flask(__name__)
import os

# python3 -m flask run
import simfin as sf
from simfin.names import *

sf.set_api_key('a3dde4ef-6674-4b65-84a3-a9ff2e7c81f2')
sf.set_data_dir(os.getcwd()+'/simfin_data/')
df = sf.load_income(variant='annual', market='us')

@app.route("/")
def home():
    return "Hello World! I'm using Flask."

@app.route("/stockdata")
def stockdata():
    print(df.loc['MSFT', [REVENUE, NET_INCOME]])
    return "df.loc['MSFT', [REVENUE, NET_INCOME]]"