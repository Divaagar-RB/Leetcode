import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views["author_id"]==views["viewer_id"]]
    df = df.sort_values(by='author_id')
    df1=df.drop_duplicates(subset=['author_id'])
    df1['id']=df1["author_id"]
    
    return df1[['id']]
    