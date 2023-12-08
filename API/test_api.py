import json
from fastapi.testclient import testclient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import app

#Create a test database
TEST_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)
app.dependency_overrides[get_db] = get_test_db

client = TestClient(app)

#Test endpoint for root path
def test_read_root():
    response = client.get("/")
    #Assert that the response is OK
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

# Test endpoint for a non-existent path
def test_read_nonexistent_path():
    # Make a request to a non-existent path
    response = client.get("/nonexistent-path")
    # Assert that the response is Not Found(Error)
    assert response.status_code == 404

#Test creating a new user
def test_create_user():
    email = "test@example.com"
    response = client.post("/create-user", json={"email": email})
    #Assert that the response is OK
    assert response.status_code = 200
    #Asser that the response is matching
    assert response.json() == {"Status": f"create user {email}"}

# Test creating a duplicate user
def test_create_duplicate_user():
    email = "test@example.com"
    response = client.post("/create-user", json={"email": email})
    #Assert that the response is OK
    assert response.status_code == 200
    assert response.json() == {"status": f"user {email} already exists"}

# Test the rated movies endpoint
def test_rated_movies():
    email = "test@example.com"
    # Assuming the user exists and has rated some movies
    response = client.get(f"/rated-movies?email={email}")
    #Assert that the response is OK
    assert response.status_code == 200
    assert "data" in response.json()

#Test the rated movies endpoint with a non-existing user
def test_rated_movies_non_existing_user():
    email = "nonexistent@example.com"
    response = client.get(f"/rated-movies?email={email}")
    #Assert that the response is OK
    assert response.status_code == 200
    assert response.json() == {"data": []}

#Test updating the rating
def test_update_rating():
    #Create a user and a movie for testing
    test_create_user()
    response_create_movie = client.post("/create-movie", json={"name": "Test Movie", "description": "Test Description", "imageUrl": "test.jpg"})
    #Assert that the response is OK
    assert response_create_movie.status_code == 200

    #Movie ID from response
    movie_id = response_create_movie.json()["id"]

    # Rate the movie for the user
    response_rate_movie = client.post("/rate-movie", json={"email": "newuser@example.com", "movieId": movie_id, "newRating": 4})
    #Assert taht the response is OK
    assert response_rate_movie.status_code == 200
    assert response_rate_movie.json() == {"result": "success"}

    #Update the rating for the same user and movie
    response_update_rating = client.post("/update-rating", json={"email": "newuser@example.com", "movieId": movie_id, "newRating": 5})
    #Assert that the response is OK
    assert response_update_rating.status_code == 200
    assert response_update_rating.json() == {"result": "success"}

    #Check the rating for updates
    response_get_rated_movies = client.get("/rated-movies", params={"email": "newuser@example.com"})
    #Asser that the response is OK
    assert response_get_rated_movies.status_code == 200
    rated_movies = response_get_rated_movies.json()["data"]

    #Find the movie by ID on rated movie lists
    updated_movie = next((movie for movie in rated_movies if movie["id"] == movie_id), None)
    assert updated_movie is not None
    # Assert rating for movie was updated to 5
    assert updated_movie["rating"] == 5