import React, { useState, useEffect } from 'react';
import MovieCard from '../MovieCard';

type Movie = {
  id: number;
  imageUrl: string;
  name: string;
  description: string;
};

const MovieList: React.FC = () => {
  const [movies, setMovies] = useState<Movie[]>([]);

  useEffect(() => {
    const fetchedMovies: Movie[] = [
        { id: 1, imageUrl: 'url1', name: 'Movie 1', description: 'Description 1' },
        { id: 2, imageUrl: 'url2', name: 'Movie 2', description: 'Description 2' },
        // ... other movies
    ];
    setMovies(fetchedMovies);
  }, []);

  return (
    <div className='container mx-auto px-4'>
      <div className='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4'>
        {movies.map(movie => (
          <MovieCard key={movie.id} {...movie} />
        ))}
      </div>
    </div>
  );
}

export default MovieList;
