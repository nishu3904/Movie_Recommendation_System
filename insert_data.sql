USE MovieStreamingDB;

-- Insert Users
INSERT INTO Users (name, age) VALUES 
('Rahul', 22), ('Sneha', 28), ('Amit', 35), ('Priya', 24), ('Vikram', 30), ('Sonia', 27);

-- Insert Movies
INSERT INTO Movies (title, genre) VALUES 
('Inception', 'Sci-Fi'), ('Interstellar', 'Sci-Fi'), ('The Matrix', 'Sci-Fi'),
('The Dark Knight', 'Action'), ('Gladiator', 'Action'), ('John Wick', 'Action'),
('The Godfather', 'Crime'), ('Pulp Fiction', 'Crime'), ('Joker', 'Crime'),
('Toy Story', 'Animation'), ('Finding Nemo', 'Animation'), ('Shrek', 'Animation');

-- Insert Ratings
INSERT INTO Ratings (user_id, movie_id, rating) VALUES 
(1,1,5), (1,2,4), (1,4,3), (2,1,5), (2,3,5), (3,7,5), (3,8,4), (3,9,5),
(5,7,4), (5,4,5), (4,10,5), (4,11,4), (4,1,5), (6,10,5), (6,12,4),
(1,7,2), (2,10,3), (3,1,4), (5,9,5);

-- Insert Watch History
INSERT INTO Watch_History (user_id, movie_id, watch_date) VALUES 
(1,1,'2024-04-10'), (2,1,'2024-04-11'), (3,1,'2024-04-12'),
(4,10,'2024-04-13'), (6,10,'2024-04-14'), (5,4,'2024-04-15'), 
(3,7,'2024-04-15'), (1,2,'2024-04-16'), (2,3,'2024-04-16'), (5,8,'2024-04-16');
