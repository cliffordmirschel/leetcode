import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    print(employees.salary)
    # Step 1: Select the column
    salary_column = employees['salary']

    # Step 2: Apply a function to each value
    def multiply(x):
        return x * 2

    new_salary_column = salary_column.apply(multiply)

    # Step 3: Assign the new values back to the column
    employees['salary'] = new_salary_column
    return employees