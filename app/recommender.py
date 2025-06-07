import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

#This loads the .csv file I got
csv_path = os.path.join(os.path.dirname(__file__), 'data', 'animes.csv')

anime_df = pd.read_csv(csv_path)

# print(anime_df.head())

#this removes any anime that has a missing synopsis or name
anime_df = anime_df[anime_df['synopsis'].notna() & anime_df['title'].notna()].reset_index(drop=True)

#since removing the anime might cause the .csv to skip indexes, here we drop the old index and reset the new one so it forgets about the previous indexes we deleted
# anime_df = anime_df.reset_index(drop=True)

#This creates an instance of TfidfVectorizer. stop_words english means it will automatically ignore commond english words like "the" and "and" because they dont add much meaning
tfidf = TfidfVectorizer(stop_words='english')

#takes the synopsis column of the dataframe and learns the vocabulary (aside from the stop words). Each synopsis gets turned into a TF-IDF vector. Which shows how important each word
# in the synopsis is compared to others. 
tfidf_matrix = tfidf.fit_transform(anime_df['synopsis'])

#Here we take two matrices and calculates the cosine similarity between every pair of anime synopsis. Linear Kernel computes the dot product of the rows of the first and second matrix.
#When you do linear kernel you are comparing each anime's TF-IDF vector to every other anime's TF-IDF vector including itself
#cosine_sim is a square matrix where i,j is the cosine similarity score between first and second anime. The diagnol where first=second will have a similarity of 1 which means the anime is 
# identical to itself
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

#This creates a pandas series. The values are the original row indices aka anime_df.index and the index are the anime names from anime_df. Any duplicates get removed.
# indices = pd.Series(anime_df.index, index=anime_df['title']).drop_duplicates()
indices = pd.Series(anime_df.index, index=anime_df['title'])
indices = indices[~indices.index.duplicated(keep='first')]


def recommend_anime(title, num_recommondations=5):
    if title not in indices:
        return ["Anime not found."]

    table = indices[title]
    all_scores = list(enumerate(cosine_sim[table].flatten()))
    sorted_scores = sorted(all_scores, key=lambda x: x[1], reverse=True)
    top_scores = sorted_scores[1:num_recommondations+1]
    
    anime_indices = [i[0] for i in top_scores]

    return anime_df['title'].iloc[anime_indices].tolist()

print(recommend_anime("Naruto"))
