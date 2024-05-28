import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students = students.astype({'grade': int})
    return students
# Optimized 
def change_datatype(students: pd.DataFrame) -> pd.DataFrame:
    students["grade"]=students["grade"].astype(int)
    return students