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

-- Sample Query 1: Retrieve all users
SELECT * FROM users;

-- Sample Query 2: Retrieve all movies
SELECT * FROM movies;

-- Sample Query 3: Add a new user
INSERT INTO users (username, password, preferences) VALUES ('john_doe', 'password123', '{"genre": "Drama", "language": "English"}');

-- Sample Query 4: Add a new movie
INSERT INTO movies (title, summary, image_url) VALUES ('Sample Movie', 'A great movie', 'http://example.com/image.jpg');

-- Sample Query 5: Retrieve users and their preferences
SELECT username, preferences FROM users;

-- Sample Query 6: Retrieve movies with a specific genre
SELECT title, summary FROM movies WHERE 'Action' = ANY(string_to_array(genres, ', '));

-- Sample Query 7: Update user preferences
UPDATE users SET preferences = '{"genre": "Comedy", "language": "Spanish"}' WHERE username = 'john_doe';

-- Sample Query 8: Delete a movie
DELETE FROM movies WHERE title = 'Sample Movie';

-- Sample Query 9: Count the number of users
SELECT COUNT(*) FROM users;

-- Sample Query 10: Count the number of movies
SELECT COUNT(*) FROM movies;

