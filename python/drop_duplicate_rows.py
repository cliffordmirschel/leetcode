import pandas as pd
# First attempt
def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers.drop_duplicates(subset=['email'], keep='first', inplace=True)
    return customers

# Optimized 

def drop_duplicate_emails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates('email', keep='first')
