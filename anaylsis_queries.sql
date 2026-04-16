USE MovieStreamingDB;

-- 1. Find Top-Rated Movies
SELECT m.title, AVG(r.rating) as avg_rating
FROM Movies m JOIN Ratings r ON m.movie_id = r.movie_id
GROUP BY m.title HAVING avg_rating >= 4.0 ORDER BY avg_rating DESC;

-- 2. Identify Most Popular Genres
SELECT m.genre, COUNT(wh.watch_id) as views
FROM Movies m JOIN Watch_History wh ON m.movie_id = wh.movie_id
GROUP BY m.genre ORDER BY views DESC;

-- 3. Recommend Movies (Similar Users - Example for Rahul)
SELECT DISTINCT m.title FROM Movies m JOIN Ratings r ON m.movie_id = r.movie_id
WHERE r.user_id IN (
    SELECT user_id FROM Ratings WHERE movie_id IN (SELECT movie_id FROM Ratings WHERE user_id = 1) AND user_id != 1
) AND m.movie_id NOT IN (SELECT movie_id FROM Watch_History WHERE user_id = 1);

-- 4. User Behavior Patterns
SELECT u.name, COUNT(r.movie_id) as rated, AVG(r.rating) as avg_score
FROM Users u LEFT JOIN Ratings r ON u.user_id = r.user_id
GROUP BY u.name;

-- 5. Detect Trending Movies
SELECT m.title, COUNT(wh.watch_id) as views FROM Watch_History wh
JOIN Movies m ON wh.movie_id = m.movie_id
GROUP BY m.title ORDER BY views DESC LIMIT 5;
