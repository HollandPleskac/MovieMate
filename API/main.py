from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Define the Movie class
class Movie(BaseModel):
    name: str
    description: str

# Create an instance of FastAPI
app = FastAPI()

# In-memory database (for demonstration purposes)
movies_db = []

@app.get("/movies", response_model=List[Movie])
async def get_movies():
    return movies_db

@app.post("/movies", response_model=Movie)
async def add_movie(movie: Movie):
    movies_db.append(movie)
    return movie