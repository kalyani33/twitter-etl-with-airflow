import pandas as pd
from datetime import datetime

def run_twitter_etl():
    
    #Step1 : Extract/Read data
    twitter_df = pd.read_csv('tweets.csv',header='infer')
    
    #Step2: Transform the data
    twitter_df = twitter_df.drop(columns=['latitude','longitude','id','language'])
    twitter_df = twitter_df.astype({'number_of_likes':'int','number_of_shares':'int'})
    #print(twitter_df.info())
    twitter_df['date_time'] = pd.to_datetime(twitter_df['date_time'],format='%d/%m/%Y %H:%M')
    twitter_df = twitter_df.fillna({"country":"USA","date_time":datetime.now()})
    
    #Step3: Load the data to S3 bucket
    twitter_df.to_csv("s3://twitter-data-analysis/twitter_analysis_data.csv",index=False)
