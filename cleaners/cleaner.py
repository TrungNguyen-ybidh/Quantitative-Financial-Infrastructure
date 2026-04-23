import ast
import pandas as pd
from config import engine
from fetchers.fetcher import Fetcher 
from sqlalchemy import text
from pathlib import Path
import os
import shutil

class Cleaner:
    """Clean FMP fundamentals data: parse dict columns, keep/rename/drop fields."""
    def __init__(self, root):
        self.root = Path(root) if root else Path.cwd().parent

    def ff_factor_clean(self, df, monthly=False, quarterly=False):
        '''
        make sure that when convert to csv, set infex = FALSE
        '''

        df.columns= df.columns.str.lower()
        df_clean = df.rename(columns={
            'unnamed: 0': 'date', 
            'mkt-rf': 'market_excess_return', 
            'smb': 'size_factor', 
            'hml': 'value_factor', 
            'rmw': 'profitability_factor', 
            'cma': 'inveatment_factor', 
            'rf': 'risk_free_rate'
        })
        df_clean['date'] = pd.to_datetime(df_clean['date'].astype('str'), format='%Y%m%d')

        if monthly or quarterly:
            df_clean = df_clean.set_index('date')
            if monthly:
                return df_clean.resample('ME').sum().round(2).reset_index()
            else:
                return df_clean.resample('QE').sum().round(2).reset_index()
        
        return df_clean

    def data_cleaning(self, df, existent=True):
        if existent:
            df.columns = df.columns.str.lower()
            existing = pd.read_sql("SELECT ticker FROM companies", engine)
            df_clean = df[df['ticker'].isin(existing['ticker'])].copy()
        else:
            df_clean = df.copy()

        date_cols = [col for col in df.columns if 'date' in col.lower()]
        
        for col in date_cols:
            df_clean[col] = pd.to_datetime(df_clean[col], errors='coerce')
        
        if 'period' in df.columns and 'date' in df.columns:
            df_clean = df_clean.drop_duplicates(subset=['ticker', 'date', 'period'], keep='first')
        elif 'date' in df.columns:
            df_clean = df_clean.drop_duplicates(subset=['ticker', 'date'], keep='first')
        else:
            df_clean = df_clean.drop_duplicates()
        
        return df_clean

    def insert_to_sql(self, table, update=True, clean=True, replace=False, exist=False ,file=None, df=None, conflict_cols=["ticker", "date"]):

        if df is None and file is not None:
            df = pd.read_csv(f"{self.root}/cleaned/{file}")
            print(f"{file}: {list(df.columns)}")
            if clean:
                if exist:
                    df_clean = self.data_cleaning(df)
                else:
                    df_clean = self.data_cleaning(df, existent=False)

        elif df is not None:
            print(f"{table}: {list(df.columns)}")
            df_clean = self.data_cleaning(df)

        if replace:
            with engine.connect() as conn:
                conn.execute(text("SET FOREIGN_KEY_CHECKS = 0"))
                conn.execute(text(f"TRUNCATE TABLE {table}"))
                conn.execute(text("SET FOREIGN_KEY_CHECKS = 1"))
                conn.commit()
                df_clean.to_sql(table, conn, if_exists="append", index=False)
                conn.commit()
            return

        elif update:
            # Skip duplicates, only insert new rows
            df_clean.to_sql("temp_staging", engine, if_exists="replace", index=False)
            cols = ", ".join([f"`{c}`" for c in df_clean.columns])
            conflict = ", ".join(conflict_cols)
            with engine.connect() as conn:
                conn.execute(text(f"""
                    INSERT IGNORE INTO {table} ({cols})
                    SELECT {cols} FROM temp_staging
                """))
                conn.execute(text("DROP TABLE temp_staging"))
                conn.commit()
        else:
            df_clean.to_sql(table, engine, if_exists="append", index=False)


    def parse_dict_col(self, file_path=None, col=None, col_lst=None):
        file_path = file_path or self.root
        fetcher = Fetcher()
        df = pd.read_csv(file_path, low_memory=False)
        if col is None and col_lst is not None:
            for col in col_lst:
                try: 
                    expanded = pd.json_normalize(df[col])
                    df = pd.concat([df.drop(columns=[col]), expanded], axis=1)
                except Exception as e:
                        df[col] = df[col].apply(ast.literal_eval)
                        expanded = pd.json_normalize(df[col])
                        df = pd.concat([df.drop(columns=[col]), expanded], axis=1)
            fetcher.save_csv(df, file_path=file_path)
            return df
        if col is not None and col_lst is None:
            try: 
                expanded = pd.json_normalize(df[col])
                df = pd.concat([df.drop(columns=[col]), expanded], axis=1)
                return df
            except Exception as e:
                df[col] = df[col].apply(ast.literal_eval)
                expanded = pd.json_normalize(df[col])
                df = pd.concat([df.drop(columns=[col]), expanded], axis=1)
                fetcher.save_csv(df, file_path=file_path)
                return df
            
    def clean_dir(self):
        cleaned_dir = f"{self.root}/cleaned"
        if os.path.exists(cleaned_dir):
            shutil.rmtree(cleaned_dir)
            print(f"Removed {cleaned_dir}")

    
class FMPCleaner(Cleaner):
    def __init__(self, root):
        super().__init__(root)

    def keep_and_rename(self, schema_map=None, input_file=None, action=None):
        input_file = input_file or self.root
        output_file = Path(f"{input_file}/cleaned")
        output_file.mkdir(exist_ok=True)
        result = {}
        fetcher = Fetcher()

        for key, value in schema_map.items():
            try:
                df = pd.read_csv(f"{input_file}/{key}", low_memory=False)

                if action is None:
                    # default: keep columns then rename
                    df = df[value["keep"]]
                    df = df.rename(columns=value["rename"])
                elif action == "keep":
                    df = df[value["keep"]]
                elif action == "rename":
                    df = df.rename(columns=value["rename"])
                elif action == "drop":
                    df = df.drop(columns=value["drop"])

                fetcher.save_csv(df, file_path=f"{output_file}/{key}")
                result[key] = df
            except Exception as e:
                print(f"{key} — {e}")

        return result