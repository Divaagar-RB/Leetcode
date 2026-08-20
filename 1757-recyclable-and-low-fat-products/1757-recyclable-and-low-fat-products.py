import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    df = products[products['recyclable']=='Y']
    df = df[df['low_fats']=='Y']
   
    return df[['product_id']]
    