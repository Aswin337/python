import pymysql
import pandas as pd
from datetime import datetime
import os

def fetch_data_from_mysql():
    mysql_config={
        "host" : "localhost",
        "user" :"root",
        "password" : "root",
        "database":"etl_example"
    }
    connection=pymysql.connect(**mysql_config)
    query="select * from sample_data"
    df=pd.read_sql(query,connection)
    connection.close()
    return df
def transform_data(df):
    df_transform=df[df["age"] > 30]
    return df_transform

def data_file_create(df):
    output_df="/home/aswinkumar/extract"
    os.makedirs(output_df,exist_ok=True)
    timestamp=datetime.now().strftime("%y%m%d%h%m%s")
    fle_name=f"etl_output_{timestamp}.csv"
    file_path=os.path.join(output_df,file_path)
    df.to_csv(file_path,exist_ok=False)
    print(f"data writeen to {file_path}")

def etl_process():
    df=fetch_data_from_mysql()
    df_transform=transform_data(df)
    data_file_create(df_transform)
    print("Running ETL pipeline....")

if __name__ == "__main__" :
    etl_process()
