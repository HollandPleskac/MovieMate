import pandas as pd 
from scipy.stats import pearsonr
import numpy as np

#read in the preprocessed data
UserItemMatrix = pd.read_csv('centereduseritem_matrix.csv', index_col=0)
movies_df = pd.read_csv('movies_encoded.csv')

def pearson_correlation(user1, user2):
    user1_ratings = UserItemMatrix.loc[user1]
    user2_ratings = UserItemMatrix.loc[user2]

    # Filter to keep only movies rated by both users
    common_movies = user1_ratings.notna() & user2_ratings.notna()
    user1_common_ratings = user1_ratings[common_movies]
    print(user1_common_ratings)
    user2_common_ratings = user2_ratings[common_movies]
    print(user1_common_ratings)

    # Check if there are common movies rated by both users
    if len(user1_common_ratings) > 1 and len(user2_common_ratings) > 1:
        if user1_common_ratings.equals(user2_common_ratings):
            return 1
        elif user1_common_ratings.var() > 0 and user2_common_ratings.var() > 0:
            return pearsonr(user1_common_ratings, user2_common_ratings)[0]
    return 0
    

def find_nearest_neighbor(userID, numNeighbors = 5):
    correlations = []
    user_id = userID
    for otherUser in UserItemMatrix.index:
        if user_id != otherUser:
            corr = pearson_correlation(user_id, otherUser)
            correlations.append((otherUser, corr))
        correlations.sort(key=lambda x: x[1], reverse=True)
        return correlations[:numNeighbors]
    

def predict_rating(userId, movieId, numNeighbors = 5):
    neighbors = find_nearest_neighbor(userId, numNeighbors)
    num = den = 0
    for neighbor_id, similarity in neighbors:
        neighbor_rating = UserItemMatrix.loc[neighbor_id]
        if pd.notna(neighbor_rating[movieId]):
            num += similarity * neighbor_rating[movieId]
            den += abs(similarity)
    return num/den if den != 0 else None

def reccomend_movies(userId, numReccomendations = 5):
    user_ratings = UserItemMatrix.loc[userId]
    unrated_movies = user_ratings[user_ratings.isna()].index
    predicted_ratings = [(movie_id, predict_rating(userId, movie_id)) for movie_id in unrated_movies]
    valid_predicted_ratings = [rating for rating in predicted_ratings if rating[1] is not None]
    valid_predicted_ratings.sort(key=lambda x: x[1], reverse=True)
    reccomend_movie_ids = [movie_id for movie_id,  _ in predicted_ratings[:numReccomendations]]
    return movies_df[movies_df['movieId'].isin(reccomend_movie_ids)]

recommended_movies = reccomend_movies(4,5)
print("Recommended Movies:")
print(recommended_movies)
