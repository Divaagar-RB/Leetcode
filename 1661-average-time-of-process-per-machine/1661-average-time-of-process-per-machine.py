import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    start = activity[activity["activity_type"]=="start"]
    end = activity[activity["activity_type"]=="end"]
    end.rename(columns={"timestamp":"timestamp_end"},inplace=True)
    res = pd.merge(start,end , on=['machine_id','process_id'],how='inner')
    res["processing_time"] = res["timestamp_end"]-res["timestamp"]
    res =res.groupby('machine_id').agg({'processing_time':'mean'}).reset_index()
    res["processing_time"]=res["processing_time"].round(3)
   
    return res


    