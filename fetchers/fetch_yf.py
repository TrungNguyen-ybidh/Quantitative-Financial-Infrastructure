import yfinance as yf
import pandas as pd
import os
import sys
import time

from config.utils import timer 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@timer
def fetch_yf(ticker_lst, interval="1d", period=None, start_date=None, end_date=None, chunk_size=50):
    ticker_lst = [t for t in ticker_lst if isinstance(t, str)]
    chunks = [ticker_lst[i:i+chunk_size] for i in range(0, len(ticker_lst), chunk_size)]
    
    dfs = []
    for i, chunk in enumerate(chunks):
        try:
            df = yf.download(chunk, interval=interval, period=period, start=start_date, end=end_date)
            df = df.stack(level='Ticker').reset_index()
            df.rename(columns={'level_1': 'Ticker'}, inplace=True)
            dfs.append(df)
            print(f"Chunk {i+1}/{len(chunks)} done")
            time.sleep(45)# 1 min between chunks
        except Exception as e:
            print(f"Chunk {i+1} failed — waiting 2 min: {e}")
            time.sleep(120)
            continue
    
    return pd.concat(dfs, ignore_index=True)


