import pandas as pd
# First solution
def find_products(products: pd.DataFrame) -> pd.DataFrame:
    res = products.loc[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    return res[['product_id']]

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')][['product_id']]