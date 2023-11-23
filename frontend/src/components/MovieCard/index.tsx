import React from 'react';

type MovieProps = {
  imageUrl: string;
  name: string;
  description: string;
};

const MovieCard: React.FC<MovieProps> = ({ imageUrl, name, description }) => {
  return (
    <div className='max-w-sm rounded overflow-hidden shadow-lg bg-gray-800 text-white'>
      <img className='w-full' src={imageUrl} alt={name} />
      <div className='px-6 py-4'>
        <div className='font-bold text-xl mb-2'>{name}</div>
        <p className='text-gray-300 text-base'>
          {description}
        </p>
      </div>
    </div>
  );
}

export default MovieCard;
