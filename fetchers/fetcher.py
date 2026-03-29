import pandas as pd 
import yfinance as yf
import time
from pathlib import Path
from config.endpoint_config import fmp_endpoints
import requests
from fredapi import Fred

class Fetcher:
    def __init__(self, symbols, api_key = None, rootpath = None, period=None, url=None):
        self.symbols = symbols
        self.api_key = api_key
        self.root = Path.cwd().parent
        self.period = period
        self.url = url

    def fetch_data(self):
        response = requests.get(self.url)
        df = pd.DataFrame(response.json())
        return df

    def safe_dataframe(self, response, symbol, endpoint):
        """Validate API response and return a DataFrame or None."""
        if isinstance(response, dict):
            if "Error Message" in response:
                print(f"API error for {symbol}/{endpoint}: {response['Error Message']}")
                return None
            return pd.DataFrame([response])
        elif isinstance(response, list):
            if response:
                return pd.DataFrame(response)
            return None
        else:
            print(f"Unexpected response for {symbol}/{endpoint}: {type(response)}")
            return None

    def save_csv(self, df, endpoint):
        output_path = self.root / 'data' / 'raw' / f"{endpoint}.csv"
        if output_path.exists():
            df.to_csv(output_path, mode='a', header=False, index=False)
        else:
            df.to_csv(output_path, mode='w', header=True, index=False)


    def fetch_yf(self,interval="1d", start_date=None, end_date=None, chunk_size=50):
        self.symbols = [t for t in self.symbols if isinstance(t, str)]
        chunks = [self.symbols[i:i+chunk_size] for i in range(0, len(self.symbols), chunk_size)]
        
        dfs = []
        for i, chunk in enumerate(chunks):
            try:
                df = yf.download(chunk, interval=interval, period=self.period, start=start_date, end=end_date)
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
    
    def fetch_macro_data(self, sids):
        fred = Fred(self.api_key)
        df = pd.DataFrame({
            name : fred.get_series(sid)
            for sid, name in sids.items()
        })
        df.reset_index(inplace=True)
        df.rename(columns={'index': 'date'}, inplace = True)
        return df
    
    def fetch_fmp_data(self, time_sleep=0.171, endpoints_lst=None, limit=None):
        base_url = 'https://financialmodelingprep.com/stable'
        endpoint_config = fmp_endpoints

        if endpoints_lst is None:
            for config in endpoint_config:
                endpoint = config["endpoint"]
                raw_responses = []
                for i, symbol in enumerate(self.symbols):
                    params = config["params"].copy()
                    params["apikey"] = self.api_key
                    params["symbol"] = symbol

                    url = f"{base_url}/{endpoint}"
                    try:
                        resp = requests.get(url, params=params)
                        resp.raise_for_status()
                        response = resp.json()
                    except Exception as e:
                        print(f"Request failed for {symbol}/{endpoint}: {e}")
                        time.sleep(time_sleep)
                        continue

                    if isinstance(response, list) and response:
                        raw_responses.extend(response)
                    elif isinstance(response, dict) and "Error Message" not in response:
                        raw_responses.append(response)

                    if (i + 1) % 100 == 0:
                        print(f"[{endpoint}] Progress: {i + 1} / {len(self.symbols)} fetched...")
                    time.sleep(time_sleep)

                if raw_responses:
                    self.save_csv(pd.DataFrame(raw_responses), endpoint)

        else:
            for end_point in endpoints_lst:
                dfs = []
                for i, symbol in enumerate(self.symbols):
                    params = {"apikey": self.api_key, "symbol": symbol}
                    if self.period is not None:
                        params["period"] = self.period
                    if limit is not None:
                        params["limit"] = limit

                    url = f"{base_url}/{end_point}"
                    response = requests.get(url, params=params).json()
                    df = self.safe_dataframe(response, symbol, end_point)
                    if df is not None:
                        dfs.append(df)

                    if (i + 1) % 100 == 0:
                        print(f"[{end_point}] Progress: {i + 1} / {len(self.symbols)} fetched...")
                    time.sleep(time_sleep)

                if dfs:
                    self.save_csv(pd.concat(dfs, ignore_index=True), end_point)                
