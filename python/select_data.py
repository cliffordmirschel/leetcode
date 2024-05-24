# First attempt

import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students[students['student_id'] == 101][['name', 'age']]

# Optimized solution
def select_data(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students['student_id']==101, ['name', 'age']]