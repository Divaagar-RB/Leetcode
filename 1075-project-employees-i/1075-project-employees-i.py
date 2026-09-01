import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(project,employee,how='left',on='employee_id')
    grouped = df.groupby('project_id')['experience_years'].mean().reset_index()
    grouped.rename(columns={'experience_years':'average_years'},inplace=True)
    grouped['average_years']=grouped['average_years'].round(2)
    return grouped