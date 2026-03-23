import requests
import pandas as pd
import time
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('FMP_api')

def fetch_data(url, name=''):
    response = requests.get(url)
    df = pd.DataFrame(response.json())
    return df.to_csv(name)
    
def fetch_fmp_comp_info(symbol_list, api_key):
    url = 'https://financialmodelingprep.com/stable/profile'
    dfs = []
    
    for i, symbol in enumerate(symbol_list):  
        response = requests.get(url, params={'symbol': symbol, 'apikey': api_key})
        data = response.json()
        
        if not data:
            print(f"No data for {symbol}")
            continue
        
        dfs.append(pd.DataFrame(data))
        time.sleep(0.171)
        
        if (i + 1) % 100 == 0:
            print(f"Progress: {i + 1} / {len(symbol_list)} fetched...")
    
    if not dfs:
        return pd.DataFrame()
    
    df = pd.concat(dfs, ignore_index=True)
    
    df_clean = df[[
        "cik", "symbol", "companyName", "sector", "industry",
        "exchange", "country", "currency", "marketCap",
        "ipoDate", "isActivelyTrading", "isEtf", "isAdr", "isFund"
    ]].rename(columns={
        "symbol":            "ticker",
        "companyName":       "name",
        "marketCap":         "market_cap",
        "ipoDate":           "ipo_date",
        "isActivelyTrading": "is_active",
        "isEtf":             "is_etf",
        "isAdr":             "is_adr",
        "isFund":            "is_fund"
    })               
    
    return df_clean

def fetch_income_statement(symbol_lst, api_key, period='quarter', limit=20, time_sleep=0.171):
    URL = 'https://financialmodelingprep.com/stable/income-statement'
    NUMERIC_COLS = [
        "revenue", "cost_of_revenue", "gross_profit", "operating_expense",
        "operating_income", "net_income", "ebitda", "eps", "shares_outstanding",
        "depreciation_amortization", "income_tax_expense", "income_before_tax",
        "interest_expense"
    ]
    COLUMN_SELECT = [
        "cik", "symbol", "date", "period", "revenue", "costOfRevenue",
        "grossProfit", "operatingExpenses", "operatingIncome", "netIncome",
        "ebitda", "eps", "weightedAverageShsOut", "fiscalYear",
        "depreciationAndAmortization", "incomeTaxExpense", "incomeBeforeTax",
        "interestExpense"
    ]
    COLUMN_RENAME = {
        "symbol":                      "ticker",
        "date":                        "period_date",
        "period":                      "period_type",
        "costOfRevenue":               "cost_of_revenue",
        "grossProfit":                 "gross_profit",
        "operatingExpenses":           "operating_expense",
        "operatingIncome":             "operating_income",
        "netIncome":                   "net_income",
        "weightedAverageShsOut":       "shares_outstanding",
        "fiscalYear":                  "fiscal_year",
        "depreciationAndAmortization": "depreciation_amortization",
        "incomeTaxExpense":            "income_tax_expense",
        "incomeBeforeTax":             "income_before_tax",
        "interestExpense":             "interest_expense"
    }

    dfs = []
    for i, symbol in enumerate(symbol_lst):
        params = {'symbol': symbol, 'limit': limit, 'period': period, 'apikey': api_key}
        data = requests.get(URL, params=params).json()
        if not isinstance(data, list) or len(data) == 0:
            continue
        dfs.append(pd.DataFrame(data))
        time.sleep(time_sleep)
        if (i + 1) % 100 == 0:
            print(f"Progress: {i + 1} / {len(symbol_lst)} fetched...")

    if not dfs:
        return pd.DataFrame()

    df = (
        pd.concat(dfs, ignore_index=True)
        [COLUMN_SELECT]
        .rename(columns=COLUMN_RENAME)
        .drop_duplicates(subset=["cik", "period_date"], keep="first")
    )

    df["cik"] = pd.to_numeric(df["cik"].replace("null", pd.NA), errors="coerce")
    df = df.dropna(subset=["cik"])
    df["cik"] = df["cik"].astype("Int64")

    for col in NUMERIC_COLS:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df["period_date"] = pd.to_datetime(df["period_date"], errors="coerce")
    df["fiscal_year"] = pd.to_numeric(df["fiscal_year"], errors="coerce").astype("Int64")
    df["period_type"] = df["period_type"].map(lambda x: "annual" if x == "FY" else "quarterly")

    return df


def fetch_balance_sheet(symbol_lst, api_key, period='quarter', limit=20, time_sleep=0.171):
    URL = 'https://financialmodelingprep.com/stable/balance-sheet-statement'
    NUMERIC_COLS = [
        "cash", "short_term_investment", "total_current_asset", "total_assets",
        "total_current_liabilities", "total_liabilities", "total_equity", "total_debt",
        "net_debt", "retained_earnings", "goodwill", "intangible_assets", "ppe_net",
        "long_term_debt", "short_term_debt", "stockholders_equity", "accounts_payable",
        "inventory"
    ]
    COLUMN_SELECT = [
        "cik", "symbol", "date", "period", "fiscalYear",
        "cashAndCashEquivalents", "shortTermInvestments", "totalCurrentAssets",
        "totalAssets", "totalCurrentLiabilities", "totalLiabilities", "totalEquity",
        "totalDebt", "netDebt", "retainedEarnings", "goodwill", "intangibleAssets",
        "propertyPlantEquipmentNet", "longTermDebt", "shortTermDebt",
        "totalStockholdersEquity", "accountPayables", "inventory"
    ]
    COLUMN_RENAME = {
        "symbol":                    "ticker",
        "date":                      "period_date",
        "period":                    "period_type",
        "fiscalYear":                "fiscal_year",
        "cashAndCashEquivalents":    "cash",
        "shortTermInvestments":      "short_term_investment",
        "totalCurrentAssets":        "total_current_asset",
        "totalAssets":               "total_assets",
        "totalCurrentLiabilities":   "total_current_liabilities",
        "totalLiabilities":          "total_liabilities",
        "totalEquity":               "total_equity",
        "totalDebt":                 "total_debt",
        "netDebt":                   "net_debt",
        "retainedEarnings":          "retained_earnings",
        "goodwill":                  "goodwill",
        "intangibleAssets":          "intangible_assets",
        "propertyPlantEquipmentNet": "ppe_net",
        "longTermDebt":              "long_term_debt",
        "shortTermDebt":             "short_term_debt",
        "totalStockholdersEquity":   "stockholders_equity",
        "accountPayables":           "accounts_payable",
        "inventory":                 "inventory"
    }

    dfs = []
    for i, symbol in enumerate(symbol_lst):
        params = {'symbol': symbol, 'limit': limit, 'period': period, 'apikey': api_key}
        data = requests.get(URL, params=params).json()
        if not isinstance(data, list) or len(data) == 0:
            continue
        dfs.append(pd.DataFrame(data))
        time.sleep(time_sleep)
        if (i + 1) % 100 == 0:
            print(f"Progress: {i + 1} / {len(symbol_lst)} fetched...")

    if not dfs:
        return pd.DataFrame()

    df = (
        pd.concat(dfs, ignore_index=True)
        [COLUMN_SELECT]
        .rename(columns=COLUMN_RENAME)
        .drop_duplicates(subset=["cik", "period_date"], keep="first")
    )

    df["cik"] = pd.to_numeric(df["cik"].replace("null", pd.NA), errors="coerce")
    df = df.dropna(subset=["cik"])
    df["cik"] = df["cik"].astype("Int64")

    for col in NUMERIC_COLS:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df["period_date"] = pd.to_datetime(df["period_date"], errors="coerce")
    df["fiscal_year"] = pd.to_numeric(df["fiscal_year"], errors="coerce").astype("Int64")
    df["period_type"] = df["period_type"].map(lambda x: "annual" if x == "FY" else "quarterly")

    return df


def fetch_cash_flow(symbol_lst, api_key, period='quarter', limit=20, time_sleep=0.171):
    URL = 'https://financialmodelingprep.com/stable/cash-flow-statement'
    NUMERIC_COLS = [
        "operating_cash_flow", "investing_cash_flow", "financing_cash_flow",
        "free_cash_flow", "capex", "dividends_paid", "net_change_in_cash",
        "net_income", "depreciation_amortization", "stock_based_compensation"
    ]
    COLUMN_SELECT = [
        "cik", "symbol", "date", "period", "fiscalYear",
        "operatingCashFlow", "netCashProvidedByInvestingActivities",
        "netCashProvidedByFinancingActivities", "freeCashFlow", "capitalExpenditure",
        "commonDividendsPaid", "netChangeInCash", "netIncome",
        "depreciationAndAmortization", "stockBasedCompensation"
    ]
    COLUMN_RENAME = {
        "symbol":                               "ticker",
        "date":                                 "period_date",
        "period":                               "period_type",
        "fiscalYear":                           "fiscal_year",
        "operatingCashFlow":                    "operating_cash_flow",
        "netCashProvidedByInvestingActivities": "investing_cash_flow",
        "netCashProvidedByFinancingActivities": "financing_cash_flow",
        "freeCashFlow":                         "free_cash_flow",
        "capitalExpenditure":                   "capex",
        "commonDividendsPaid":                  "dividends_paid",
        "netChangeInCash":                      "net_change_in_cash",
        "netIncome":                            "net_income",
        "depreciationAndAmortization":          "depreciation_amortization",
        "stockBasedCompensation":               "stock_based_compensation"
    }

    dfs = []
    for i, symbol in enumerate(symbol_lst):
        params = {'symbol': symbol, 'limit': limit, 'period': period, 'apikey': api_key}
        data = requests.get(URL, params=params).json()
        if not isinstance(data, list) or len(data) == 0:
            continue
        dfs.append(pd.DataFrame(data))
        time.sleep(time_sleep)
        if (i + 1) % 100 == 0:
            print(f"Progress: {i + 1} / {len(symbol_lst)} fetched...")

    if not dfs:
        return pd.DataFrame()

    df = (
        pd.concat(dfs, ignore_index=True)
        [COLUMN_SELECT]
        .rename(columns=COLUMN_RENAME)
        .drop_duplicates(subset=["cik", "period_date"], keep="first")
    )

    df["cik"] = pd.to_numeric(df["cik"].replace("null", pd.NA), errors="coerce")
    df = df.dropna(subset=["cik"])
    df["cik"] = df["cik"].astype("Int64")

    for col in NUMERIC_COLS:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df["period_date"] = pd.to_datetime(df["period_date"], errors="coerce")
    df["fiscal_year"] = pd.to_numeric(df["fiscal_year"], errors="coerce").astype("Int64")
    df["period_type"] = df["period_type"].map(lambda x: "annual" if x == "FY" else "quarterly")

    return df