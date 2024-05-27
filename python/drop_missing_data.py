import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset=['name'])

# Optimized Solution

def drop_missing_data(students: pd.DataFrame) -> pd.DataFrame:
    return students[students['name'].notnull()]