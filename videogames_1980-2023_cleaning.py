import numpy as np
import pandas as pd
import random


games_df = pd.read_csv('games.csv')
games_df.head()

def drop_missing_values(games_df, subset=None):

    return games_df.dropna(inplace=True)

drop_missing_values(games_df)

print(games_df.isnull().sum())

games_df.dtypes

games_df.rename(columns={'Release Date': 'Release_Date', 'Times Listed': 'Times_Listed','Number of Reviews': 'Num_of_Reviews'}, inplace=True)

games_df.pop('Unnamed: 0')
games_df.pop('Times_Listed')

abbreviations = {
    '3.9K': '3900',
    '2.9K': '2900',
    '4.3K': '4300',
    '3.5K': '3500',
    '3K': '3000',
    '2.3K': '2300',
    '1.6K': '1600',
    '2.1K': '2100',
    '2.7K': '2700',
    '1.5K': '1500',
    '3.4K': '3400',
    '2.8K': '2800',
    '2K': '2000',
    '1.7K': '1700',
    '1.4K': '1400',
    '1.1K': '1100',
    '2.5K': '2500',
    '2.4K': '2400', 
    '2.6K': '2600',
    '1.9K': '1900',
    '1.8K': '1800',
    '2.2K': '2200',
    '1K': '1000',
    '1.3K': '1300',
    '1.2K': '1200'
    
}

games_df['Num_of_Reviews'] = games_df['Num_of_Reviews'].replace(abbreviations)

fixed_Plays_num = {
    '17K': '17000', '21K': '21000', '30K': '30000', '28K': '28000', '33K': '33000', '7.2K': '7200', '9.2K': '9200',
    '25K': '25000', '18K': '18000', '12K': '12000', '7.7K': '7700', '29K': '29000', '20K': '20000', '15K': '15000',
    '19K': '19000', '9.1K': '9100', '3K': '3000', '14K': '14000', '13K': '13000', '5.3K': '5300', '3.9K': '3900',
    '5.9K': '5900', '6K': '6000', '6.7K': '6700', '2.2K': '2200', '9.9K': '9900', '16K': '16000', '4.1K': '4100', '8.6K': '8600', 
    '22K': '22000', '2.9K': '2900', '6.6K':'6600' , '5.4K': '5400', '3.4K': '3400', '7.5K': '7500', '10K': '10000', '9.4K': '9400',
    '11K': '11000', '9K': '9000', '3.7K': '3700', '8.4K': '8400', '1.6K': '1600', '1.2K': '1200', '4.3K': '4300', '1.1K': '1100', '6.4K': '6400',
    '5.7K': '5700', '5.6K': '5600', '7.4K': '7400', '5.1K': '5100', '2.8K': '2800', '9.6K': '9600', '9.7K': '9700', '3.5K': '3500', '9.3K': '9300', 
    '4.2K': '4200', '2.7K': '2700', '4K': '4000', '5.5K': '5500', '1.4K': '1400', '4.9K': '4900','3.1K': '3100', '1.3K': '1300',
    '2.5K': '2500', '2.6K': '2600', '7.8K': '7800', '8.5K': '8500', '6.8K': '6800', '7.9K': '7900', '6.1K': '6100', '3.2K': '3200', 
    '7.6K': '7600', '1.5K': '1500', '3.6K': '3600', '4.7K': '4700', '4.6K': '4600', '9.5K': '9500', '6.9K': '6900', '2.4K': '2400', '3.8K': '3800',
    '8.9K': '8900', '1.7K': '1700', '8.2K': '8200', '6.3K': '6300', '3.3K': '3300', '4.4K': '4400', '8.3K': '8300', '5K': '5000', '9.8K': '9800',
    '5.8K': '5800', '2.3K': '2300', '4.8K': '4800', '7.3K': '7300', '6.5K': '6500', '4.5K': '4500', '1K': '1000', '7.1K': '7100', '1.8K': '1800',
    '2.1K': '2100', '5.2K': '5200', '2K': '2000', '7K': '7000', '1.9K': '1900', '8.1K': '8100', '8.7K': '8700', '8K': '8000', '6.2K': '6200',
    '8.8K': '8800'
}

games_df['Plays'] = games_df['Plays'].replace(fixed_Plays_num)

fixed_playing_num = {
    '3.8K': '3800', '3.2K': '3200', '2.5K': '2500', '2.4K': '2400', '1.8K': '1800', '1.1K': '1100', '2.3K': '2300', '1.2K': '1200', 
    '1.7K': '1700', '1.6K': '1600', '1.5K': '1500', '2.7K': '2700', '1K': '1000', '2K': '2000'
}

games_df['Playing'] = games_df['Playing'].replace(fixed_playing_num)

games_df['Num_of_Reviews'] = games_df['Num_of_Reviews'].astype(str).astype(int)
games_df['Plays'] = games_df['Plays'].astype(str).astype(int)
games_df['Playing'] = games_df['Playing'].astype(str).astype(int)

games_df.dtypes

# Convert 'Release_Date' column to datetime objects, handling errors
games_df['Release_Date'] = pd.to_datetime(games_df['Release_Date'], errors='coerce')

# Drop rows with NaT (Not a Time) values in 'Release_Date'
games_df.dropna(subset=['Release_Date'], inplace=True)

games_df['Day'] = games_df['Release_Date'].dt.day
games_df['Month'] = games_df['Release_Date'].dt.month
games_df['Year'] = games_df['Release_Date'].dt.year