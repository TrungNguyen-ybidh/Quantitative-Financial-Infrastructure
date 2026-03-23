from fredapi import Fred
import pandas as pd 

def fetch_macro_data(sids, api_key):
    fred = Fred(api_key)
    df = pd.DataFrame({
        name : fred.get_series(sid)
        for sid, name in sids.items()
    })
    df.reset_index(inplace=True)
    df.rename(columns={'index': 'date'}, inplace = True)
    return df