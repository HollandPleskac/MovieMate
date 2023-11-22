-- Create Users table
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    preferences VARCHAR(255) -- You may want to use JSON or another format for preferences
);

-- Create Movies table
CREATE TABLE movies (
    title VARCHAR(255) NOT NULL,
    summary TEXT,
    image_url VARCHAR(255),
);
