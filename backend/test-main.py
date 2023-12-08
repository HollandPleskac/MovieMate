import pytest
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
import requests

# ---- SETUPBASE SQL DB ------

# Load environment variables from .env file
load_dotenv()

# Retrieve variables from environment
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')


Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    email = Column("email", String, primary_key=True)

    def __init__(self, email):
        self.email = email

    # for printing User objects
    def __repr__(self):
        return f"{self.email}"

class Movie(Base):
    __tablename__ = "movies"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name",String, nullable=False)
    description = Column("description", String, nullable=False)
    imageUrl = Column("imageUrl", String, nullable=False)

    # owner = Column(Integer, ForeignKey("people.ssn"))

    def __init__(self, name, description, imageUrl):
        self.name = name
        self.description = description
        self.imageUrl = imageUrl

    def __repr__(self):
        return f"({self.id}) {self.name}"


class Rating(Base):
    __tablename__ = "ratings"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    userEmail = Column(String, ForeignKey("users.email"), nullable=False)  # Reference to User.email
    movieId = Column(Integer, ForeignKey("movies.id"), nullable=False)
    rating = Column("rating", Integer, nullable=True)

    def __init__(self, userEmail, movieId, rating):
        self.userEmail = userEmail
        self.movieId = movieId
        self.rating = rating

    def __repr__(self):
        return f"({self.userEmail}) ({self.movieId}) {self.rating}"

TEST_DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

# Create an engine to the test database
engine = create_engine(TEST_DATABASE_URL)

# Use scoped_session to ensure thread safety
Session = sessionmaker(bind=engine)
db_session = Session()

# Before running this, seed the db correctly
Base.metadata.drop_all(engine)

# Create all tables
Base.metadata.create_all(engine)



def test_read_main():
    url = "http://127.0.0.1:8000/"
    response = requests.get(url)

def test_create_user_api():
    # URL for the create-user endpoint
    url = "http://127.0.0.1:8000/create-user"

    # JSON data to send in the POST request
    user_data = {"email": "test@example.com"}

    # Send a POST request
    response = requests.post(url, json=user_data)

    # Check if the user exists in the database
    user = db_session.query(User).filter_by(email="test@example.com").first()

    assert response.json() == {"status": f"create user {user_data['email']}"}

def test_create_user_already_in_db_api():
    # URL for the create-user endpoint
    url = "http://127.0.0.1:8000/create-user"

    # JSON data to send in the POST request
    user_data = {"email": "test@example.com"}

    # Send a POST request
    response = requests.post(url, json=user_data)

    # Check if the user exists in the database
    user = db_session.query(User).filter_by(email="test@example.com").first()

    assert response.json() == {"status": f"user {user_data['email']} already exists"}

def test_get_user_rated_movies_is_0_api():
    # URL for the create-user endpoint
    url = "http://127.0.0.1:8000/rated-movies?email="+"test@example.com"

    # Send a POST request
    response = requests.get(url)
    rated_movies = response.json()['data']
    assert len(rated_movies) == 0

def test_get_user_rated_movies_api():
    # URL for the create-user endpoint
    url = "http://127.0.0.1:8000/rated-movies?email="+"test@example.com"

    # Add movie
    m = Movie("Movie rated by test@example.com", "description", "https://www.twincities.com/wp-content/uploads/2022/05/Summer_Film_Preview_71939.jpg")
    db_session.add(m)
    db_session.commit()

    # # Add row to table
    m = Rating("test@example.com", m.id, 4)
    db_session.add(m)
    db_session.commit()

    # Send a POST request
    response = requests.get(url)
    rated_movies = response.json()['data']
    print(rated_movies)
    assert len(rated_movies) == 1
    assert rated_movies[0]['name'] == "Movie rated by test@example.com"

def test_user_rate_new_movie_api():
    # URL for the create-user endpoint
    url = "http://127.0.0.1:8000/rate-movie"

    # JSON data to send in the POST request
    user_data = {"email": "test@example.com", "movieId":1, "newRating":5}

    # Send a POST request
    response = requests.post(url, json=user_data)

    result = response.json()['result']
    assert result == 'success'

    results = db_session.query(Rating).join(User, "test@example.com" == Rating.userEmail).join(Movie, Movie.id == Rating.movieId).all()
    print(results[0].movieId)
    assert results[0].movieId == 1
    assert results[0].rating == 5
    assert results[0].userEmail == "test@example.com"

def test_user_change_rating_movie_api():
    # URL for the create-user endpoint
    url = "http://127.0.0.1:8000/rate-movie"

    # JSON data to send in the POST request
    user_data = {"email": "test@example.com", "movieId":1, "newRating":3}

    # Send a POST request
    response = requests.post(url, json=user_data)

    result = response.json()['result']
    assert result == 'success'

    results = db_session.query(Rating).join(User, "test@example.com" == Rating.userEmail).join(Movie, Movie.id == Rating.movieId).all()
    print(results[0].movieId)
    assert results[0].movieId == 1
    assert results[0].rating == 3
    assert results[0].userEmail == "test@example.com"
