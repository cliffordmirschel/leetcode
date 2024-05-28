import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    vertical_concat = pd.concat([df1, df2], axis=0)
    return vertical_concat

def alt_solution(df1: pd.DataFrame, df2: pd.DataFrame):
    df3 = pd.concat([df1, df2])
    return df3

