import pandas as pd
# First attempt
def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(lambda row: row.salary * 2, axis = 1)
    return employees

# Optimized soluition

def create_bonus_column(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary'] * 2
    return employees
