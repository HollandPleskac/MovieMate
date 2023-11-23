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
async def get_movies(limitL int = Query(default=10, ge=1), offset: int = Query(default=0, ge=0), search_query: str = None, db: Session = Depends(get_db)):
    #query the database for movies
    query = db.query(MovieDB)
    if search_query:
        query = query.filter(MovieDB.title.ilike(f"%{search_query}%") | MovieDB.summary.ilike(f"%{search_query}%"))
    movies = query.offset(offset).limit(limit).all()
    return [Movie(title=movie.title, summary=movie.summary, image_url=movie.image_url) for movie in movies]

@app.post("/movies/op", response_model=Movie)
async def like_dislike_movie(op: MovieOp, db: Session = Depends(get_db)):
    movie = db.query(MovieDB).filter(MovieDB.title == op.title).first()
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    if op.operation == "like":
        user = db.query(User).filter(User.username == "john_jon").first()
        user.liked_movies = True
        db.commit()
    elif op.operation == "dislike":
        user = db.query(User).filter(User.username == "john_jon").first()
        user.disliked_movies = True
        db.commit()
    else:
        raise HTTPException(status_code=400, detail="Invalid operation")

    return Movie(title=movie.title, summary=movie.summary, image_url=movie.image_url)

#get liked movies endpoint
@app.get("/movies.liked", response_model=List[Movie])
async def get_liked_movies(db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == "john_jon").first()
    if not user or no user.liked_movies:
        return[]
    
    liked_movies = db.query(MovieDB).all()

    return [Movie(title=movie.title, summary=movie.summary, image_url=movie.image_url) for movie in liked_movies]

#Get disliked movies endpoint
@app.get("/movies/disliked", response_model=List[Movie])
async def get_disliked_movies(db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == "john_jon").first()
    if not user or no user.disliked_movies:
        return []
    
    disliked_movies = db.query(MovieDB).all()

    return [Movie(title=movie.title, summary=movie.summary, image_url=movie.image_url) for movie in disliked_movies]

@app.post("/movies", response_model=Movie)
async def add_movie(movie: Movie):
    movies_db.append(movie)
    return movie