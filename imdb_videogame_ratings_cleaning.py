import numpy as np
import pandas as pd
import random

imdb_df = pd.read_csv('imdb_video_game_rating.csv')
imdb_df.head()

imdb_df.isnull().sum()
imdb_df.dtypes

imdb_df.pop('Unnamed: 0')


imdb_df['year'] = pd.to_datetime(imdb_df['year'], errors = 'coerce').dt.year
imdb_df.dropna(subset=['year'], inplace=True)



clean_votes = imdb_df['votes'].str.replace(',', '').astype(int)
imdb_df['votes'] = clean_votes
imdb_df.head()

