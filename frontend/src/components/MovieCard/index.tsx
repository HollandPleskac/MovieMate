import React from 'react';
import Image from 'next/image'

type MovieProps = {
    id: number;
    rating: number | null;
    name: string;
    description: string;
};

const MovieCard: React.FC<MovieProps> = ({ id, rating, name, description }) => {

  const handleRateMovie = async (movieId: number, newRating: number) => {
    try {
      const email = "hollandpleskac@gmail.com"; // Replace with dynamic email if needed
      const response = await fetch('http://127.0.0.1:8000/rate-movie', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email: email,
          movieId: movieId,
          newRating: newRating
        }),
      });
  
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
  
      const result = await response.json();
      console.log("Rate movie response:", result);
  
    } catch (error) {
      console.error('Failed to rate movie:', error);
    }
  }

  return (
<div className='flex flex-col justify-start items-start p-6 max-w-[348px] rounded overflow-hidden shadow-lg bg-gray-800 text-white'>
    <div className='' >
    <Image
      src={'https://lajoyalink.com/wp-content/uploads/2018/03/Movie.jpg'}
      alt={name}
      width={300}
      height={100}
    />
    </div>
    <div className='w-[300px] py-4 w-full'>
      <div className='font-bold text-xl mb-2'>{name}</div>
      <p className='text-gray-300 text-base'>
        {description}
      </p>
      <div className='flex space-x-2 mt-3'>
          {[1, 2, 3, 4, 5].map((ratingNumber) => (
            <button
              key={ratingNumber}
              className={`h-8 w-8 rounded-full border border-white flex items-center justify-center ${
                rating === ratingNumber ? 'bg-white text-gray-800' : 'text-white'
              }`}
              onClick={() => handleRateMovie(id, ratingNumber)}
            >
              {ratingNumber}
            </button>
          ))}
        </div>
    </div>
</div>
  );
}

export default MovieCard;
