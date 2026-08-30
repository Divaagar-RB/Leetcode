import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    bore = cinema['description']!= 'boring'
    odd_number = cinema['id']%2 ==1
    df = cinema[bore & odd_number]
    return df.sort_values(by='rating' , ascending=False)
    