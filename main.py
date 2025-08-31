import requests
import os
from dotenv import load_dotenv
import time
import pandas as pd
from datetime import datetime
import psycopg2

now = datetime.now()
print("Finnhub request started at: ", now)

env_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(env_path)
finnhub_api_key = os.getenv("FINNHUB_API_KEY")

conn = psycopg2.connect(
            host=os.getenv("POSTGRES_HOST"), 
            port="5432", 
            dbname=os.getenv("POSTGRES_DB_NAME"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD") 
        )
cur = conn.cursor()


dict_data = {"stock_name": [], "stock_price":[], "created_at": []}

file = open('tickers.txt', 'r')
tickers = []

for x in file: 
    x_cleaned = x.replace("\n", "") # Tickers outputed with \n, removing it
    tickers.append(str(x_cleaned)) # Pushing the cleaned tickers 
    
# print(tickers) # Test OK

headers = {
    'X-Finnhub-Token': str(finnhub_api_key),
}

for ticker in tickers: 
    
    params = { "symbol": ticker }
    url = f"https://finnhub.io/api/v1/quote"
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    dict_data["stock_name"].append(ticker)
    dict_data["stock_price"].append(data["c"])
    dict_data["created_at"].append(datetime.fromtimestamp(time.time()))

# # print(dict_data)

df = pd.DataFrame.from_dict(dict_data)
# print(df.loc[1]["stock_price"])
# print(len(df))

insert_query = """
INSERT INTO "stocks" (
    stock_name, stock_price, created_at, updated_at
) VALUES (%s, %s, %s, %s)
"""

for i in range(50): # length of the dataframe
    new_row = (
        str(df.loc[i]["stock_name"]), 
        float(df.loc[i]["stock_price"]), 
        df.loc[i]["created_at"], 
        df.loc[i]["created_at"]
    )
    
    cur.execute(insert_query, new_row)

conn.commit()
conn.close()
file.close()
print("Script executed successfully.")