import pytest
import pandas as pd
from pytest_mock import mocker
from reccomendation_algorithim import pearson_correlation, find_nearest_neighbor, predict_rating, reccomend_movies


def test_pearson_correlation():
    # Assuming user1 and user2 are valid user IDs in your test dataset
    correlation = pearson_correlation(2, 5)
    assert isinstance(correlation, (float,int))
    if isinstance(correlation, float):
        assert -1.0 <= correlation <= 1.0
    else:
        assert correlation == 0

def test_pearson_identical_ratings(mocker):
    # Choose user IDs with identical ratings for their common movies
    correlation = pearson_correlation(1, 2)
    assert correlation == 1

def test_pearson_no_common_movies():
    # Choose user IDs that have no common movies rated
    correlation = pearson_correlation(2,3)
    assert correlation == 0

def test_pearson_one_common_movie():
    # Choose user IDs that have exactly one common movie rated
    correlation = pearson_correlation(3, 4)
    assert correlation == 0

def test_pearson_opposite_ratings():
    # Choose user IDs with opposite ratings for their common movies
    correlation = pearson_correlation(5, 6)
    assert correlation < 0

def test_find_nearest_neighbor():
    # Test with a valid user ID
    neighbors = find_nearest_neighbor(1, 5)
    assert isinstance(neighbors, list)
    assert len(neighbors) <= 5
    # Optionally, check the type of elements in neighbors, etc.

def test_predict_rating():
    # Test with a valid user ID and movie ID
    rating = predict_rating(1, 8)  # Assuming movie ID 10 exists in your mock data
    assert isinstance(rating, float) or rating is None
    if rating is not None:
        assert 0.0 <= rating <= 5.0  # Assuming the rating scale is 0 to 5

def test_recommend_movies():
    recommendations = reccomend_movies(1,5)
    assert isinstance(recommendations, pd.DataFrame)
    assert len(recommendations) <= 5  # Checks if 5 or fewer recommendations are returned
    

