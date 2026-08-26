import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    res = pd.merge(sales,product,on='product_id',how='inner')
    return res[["product_name","year","price"]]
    