import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(students,subjects,how='cross')
    df2= examinations.value_counts()
    res = pd.merge(df, df2,how='left',on=['student_id','subject_name'])
    res["count"] = res["count"].fillna(0)
    res["count"]=res["count"].astype('int')
    res.rename(columns={"count":"attended_exams"},inplace=True)
    res.sort_values(by=['student_id','subject_name'],inplace=True)
    return res
    