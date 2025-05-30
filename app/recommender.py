import pandas as pd
import os

#This loads the .csv file I got
csv_path = os.path.join(os.path.dirname(__file__), 'data', 'animes.csv')

anime_df = pd.read_csv(csv_path)

# print(anime_df.head())