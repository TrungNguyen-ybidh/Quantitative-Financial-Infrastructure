import ast
import pandas as pd
from config.config import ROOT
from fetchers.fetcher import Fetcher 


def parse_dict_col(file_path, col=None, col_lst=None):
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

def keep_and_rename(schema_map, input_file = ROOT, output_file = ROOT, action=None):
    result = {}
    fetcher = Fetcher()
    if action is None:
        for key, value in schema_map.items():
            try:
                df = pd.read_csv(f"{input_file}/{key}", low_memory=False)
                df = df[value["keep"]]
                df = df.rename(columns=schema_map[key]['rename'])
                fetcher.save_csv(df, file_path=f"{output_file}/{key}")
                result[key] = df
            except Exception as e:
                 print(f"{key} — {e}")
        return result
    elif action == 'rename':
        for key, value in schema_map.items():
            try:
                df = pd.read_csv(f"{input_file}/{key}", low_memory=False)
                df = df.rename(columns=schema_map[key][action])
                fetcher.save_csv(df, file_path=f"{output_file}/{key}")
                result[key] = df
            except Exception as e:
                print(f"{key} - {e}")
        return result
    elif action == 'drop':
        for key, value in schema_map.items():
            try:
                df = pd.read_csv(f"{input_file}/{key}", low_memory=False)
                df = df.drop(columns=schema_map[key][action])
                fetcher.save_csv(df, file_path=f"{output_file}/{key}")
                result[key] = df
            except Exception as e:
                print(f"{key} - {e}")
        return result
    elif action == 'keep':
        for key, value in schema_map.items():
            try:
                df = pd.read_csv(f"{input_file}/{key}", low_memory=False)
                df = df[value[action]]
                fetcher.save_csv(df, file_path=f"{output_file}/{key}")
                result[key] = df
            except Exception as e:
                print(f"{key} - {e}")
        return result