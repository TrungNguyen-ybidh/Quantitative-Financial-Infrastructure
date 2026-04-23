import time
import requests
import pandas as pd
import yfinance as yf
from pathlib import Path
from fredapi import Fred
from config.fmp_config import fmp_endpoints



class Fetcher:
    """Shared utilities: HTTP helpers, CSV I/O, DataFrame validation."""

    def __init__(self, symbols=None, api_key=None, root=None):
        self.symbols = symbols or []
        self.api_key = api_key
        self.root = Path(root) if root else Path.cwd().parent

    def _get_json(self, url, params=None):
        resp = requests.get(url, params=params)
        resp.raise_for_status()
        return resp.json()

    def safe_dataframe(self, response, symbol="", endpoint=""):
        if isinstance(response, dict):
            if "Error Message" in response:
                print(f"API error for {symbol}/{endpoint}: {response['Error Message']}")
                return None
            return pd.DataFrame([response])
        elif isinstance(response, list):
            return pd.DataFrame(response) if response else None
        else:
            print(f"Unexpected response for {symbol}/{endpoint}: {type(response)}")
            return None

    def save_csv(self, df, file_path=None, endpoint=None):
        file_path = Path(file_path or self.root)
        output_path = file_path / f"{endpoint}.csv" if endpoint else file_path

        if output_path.exists():
            df.to_csv(output_path, mode='a', header=False, index=False)
        else:
            df.to_csv(output_path, mode='w', header=True, index=False)


class FMPFetcher(Fetcher):
    """Fetch fundamentals from Financial Modeling Prep."""

    BASE_URL = "https://financialmodelingprep.com/stable"

    def __init__(self, symbols=None, api_key=None, root=None, time_sleep=0.08):
        super().__init__(symbols, api_key, root)
        self.time_sleep = time_sleep

    def fetch_all(self, file_path=None, endpoint_config=None):
        """
        Walk every entry in endpoint_config (defaults to the imported list)
        and save one CSV per endpoint.
        """
        file_path = file_path or self.root
        endpoint_config = endpoint_config or fmp_endpoints

        for config in endpoint_config:
            endpoint = config["endpoint"]
            raw_responses = []

            for i, symbol in enumerate(self.symbols):
                params = config["params"].copy()
                params["apikey"] = self.api_key
                params["symbol"] = symbol

                try:
                    response = self._get_json(f"{self.BASE_URL}/{endpoint}", params=params)
                except Exception as e:
                    print(f"Request failed for {symbol}/{endpoint}: {e}")
                    time.sleep(self.time_sleep)
                    continue

                if isinstance(response, list) and response:
                    raw_responses.extend(response)
                elif isinstance(response, dict) and "Error Message" not in response:
                    raw_responses.append(response)

                if (i + 1) % 100 == 0:
                    print(f"[{endpoint}] Progress: {i + 1} / {len(self.symbols)} fetched...")
                time.sleep(self.time_sleep)

            if raw_responses:
                self.save_csv(pd.DataFrame(raw_responses), endpoint=endpoint, file_path=file_path)

    def fetch_endpoints(self, endpoints_lst, file_path=None, period=None, limit=None):
        """
        Fetch a custom list of endpoints with optional period/limit overrides.
        Useful for ad-hoc pulls outside the main config.
        """
        file_path = file_path or self.root

        for end_point in endpoints_lst:
            dfs = []

            for i, symbol in enumerate(self.symbols):
                params = {"apikey": self.api_key, "symbol": symbol}
                if period is not None:
                    params["period"] = period
                if limit is not None:
                    params["limit"] = limit

                try:
                    response = self._get_json(f"{self.BASE_URL}/{end_point}", params=params)
                except Exception as e:
                    print(f"Request failed for {symbol}/{end_point}: {e}")
                    time.sleep(self.time_sleep)
                    continue

                df = self.safe_dataframe(response, symbol, end_point)
                if df is not None:
                    dfs.append(df)

                if (i + 1) % 100 == 0:
                    print(f"[{end_point}] Progress: {i + 1} / {len(self.symbols)} fetched...")
                time.sleep(self.time_sleep)

            if dfs:
                self.save_csv(pd.concat(dfs, ignore_index=True), endpoint=end_point, file_path=file_path)


class YFinanceFetcher(Fetcher):
    """Fetch OHLCV price data from Yahoo Finance."""

    def __init__(self, symbols=None, root=None, chunk_size=50):
        super().__init__(symbols, root=root)
        self.chunk_size = chunk_size

    def fetch(self, interval="1d", timesleep=45, period=None, start_date=None, end_date=None, csv=False):
        symbols = [t for t in self.symbols if isinstance(t, str)]
        chunks = [symbols[i:i + self.chunk_size]
                for i in range(0, len(symbols), self.chunk_size)]

        for i, chunk in enumerate(chunks):
            try:
                df = yf.download(chunk, interval=interval, period=period,
                                start=start_date, end=end_date)
                df = df.stack(level='Ticker').reset_index()
                df.rename(columns={'level_1': 'Ticker'}, inplace=True)
                
                mode = 'w' if i == 0 else 'a'
                header = i == 0
                df.to_csv(f"{self.root}/daily_prices.csv", mode=mode, header=header, index=False)
                
                print(f"Chunk {i + 1}/{len(chunks)} done")
                time.sleep(timesleep)

            except Exception as e:
                print(f"Chunk {i + 1} failed — waiting 2 min: {e}")
                time.sleep(120)
                continue

        if csv:
            return pd.read_csv(f"{self.root}/daily_prices.csv")
        
        return pd.read_csv(f"{self.root}/daily_prices.csv")



class FREDFetcher(Fetcher):
    """Fetch macroeconomic series from FRED."""

    def __init__(self, api_key=None, root=None):
        super().__init__(api_key=api_key, root=root)

    def fetch(self, series_map):
        fred = Fred(self.api_key)
        results = {}
        
        for sid, name in series_map.items():
            try:
                results[name] = fred.get_series(sid)
            except ValueError as e:
                print(f"Skipping {sid} ({name}): {e}")
                continue
        
        if not results:
            print("No valid series found.")
            return pd.DataFrame()
        
        df = pd.DataFrame(results)
        df.reset_index(inplace=True)
        df.rename(columns={'index': 'date'}, inplace=True)
        return df