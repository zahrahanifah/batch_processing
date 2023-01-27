import pandas as pd
import os
import glob
import psycopg2
from datetime import datetime

#connect to postgresql
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=1234")
cur = conn.cursor()

#read file in directory
path = os.getcwd()
folder = glob.glob(os.path.join("E:/Zahra - Data Bootcamp/batch_processing/source", "*.csv"))

#create query to insert multiple python variable in sql
for file in folder:
    df= pd.read_csv(file,sep=";")
           
    filename = str(file.split("\\")[-1])
    current_time = datetime.now()

    for index, row in df.iterrows():
        cur.execute("INSERT INTO all_ticket VALUES (%s, %s, %s, %s, %s, %s, %s) on conflict do nothing",(row['no_ticket'], row['title'], row['body'], row['created_on'], row['ticket_status'], filename, current_time))
    
conn.commit()

print("Create Table Success")




