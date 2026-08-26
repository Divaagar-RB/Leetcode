import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    res = pd.merge(employees , employee_uni , on="id" , how="outer")
    # res = res["name"].dropna()
    res.dropna(axis=0 , subset=["name"],inplace=True)
    return res[["unique_id","name"]]
    