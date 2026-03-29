import requests
import pandas as pd
import time
from dotenv import load_dotenv
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.endpoint_config import fmp_endpoints
from config.utils import timer
from pathlib import Path

load_dotenv()
api_key = os.getenv('FMP_api')

def fetch_data(url):
    response = requests.get(url)
    df = pd.DataFrame(response.json())
    return df

@timer
def fetch_fmp_data(symbols, api_key, time_sleep=0.171, endpoints_lst=None, period=None, limit=None):
    ROOT = Path.cwd().parent
    base_url = 'https://financialmodelingprep.com/stable'
    endpoint_config = fmp_endpoints

    def safe_dataframe(response, symbol, endpoint):
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

    def save_csv(df, endpoint):
        output_path = ROOT / 'data' / 'raw' / f"{endpoint}.csv"
        if output_path.exists():
            df.to_csv(output_path, mode='a', header=False, index=False)
        else:
            df.to_csv(output_path, mode='w', header=True, index=False)

    if endpoints_lst is None:
        for config in endpoint_config:
            endpoint = config["endpoint"]
            raw_responses = []
            for i, symbol in enumerate(symbols):
                params = config["params"].copy()
                params["apikey"] = api_key
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
                    print(f"[{endpoint}] Progress: {i + 1} / {len(symbols)} fetched...")
                time.sleep(time_sleep)

            if raw_responses:
                save_csv(pd.DataFrame(raw_responses), endpoint)

    else:
        for end_point in endpoints_lst:
            dfs = []
            for i, symbol in enumerate(symbols):
                params = {"apikey": api_key, "symbol": symbol}
                if period is not None:
                    params["period"] = period
                if limit is not None:
                    params["limit"] = limit

                url = f"{base_url}/{end_point}"
                response = requests.get(url, params=params).json()
                df = safe_dataframe(response, symbol, end_point)
                if df is not None:
                    dfs.append(df)

                if (i + 1) % 100 == 0:
                    print(f"[{end_point}] Progress: {i + 1} / {len(symbols)} fetched...")
                time.sleep(time_sleep)

            if dfs:
                save_csv(pd.concat(dfs, ignore_index=True), end_point)                

