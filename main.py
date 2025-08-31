import requests
import os
from dotenv import load_dotenv
import time
import pandas as pd
from datetime import datetime

env_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(env_path)
finnhub_api_key = os.getenv("FINNHUB_API_KEY")
# print(finnhub_api_key)

dict_data = {"stock_name": [], "stock_price":[], "created_at": []}

tickers = ["GOOGL", "TSLA", "AAPL", "NVDA", "MSFT", "AMZN", "META", "LLY", "ORCL", "NFLX"]

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

# print(dict_data)

df = pd.DataFrame.from_dict(dict_data)
print(df)
df.to_csv("financial_data.csv", mode="a", header=False, index=False)
# print(type(time.gmtime(dict_data["time"][0])))