import streamlit as st
import mysql.connector
import pandas as pd

# Database Connection Function
def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="nishu123", # Replace with your MySQL password
        database="MovieStreamingDB"
    )

# Page Setup
st.set_page_config(page_title="Movie Recommendation System", layout="wide")
st.title("🎬 Movie Analysis Mini-Project")
st.write("A simple SQL-based recommendation and rating analysis system.")

# Sidebar Navigation
st.sidebar.header("Navigation")
feature = st.sidebar.radio("Go to:", [
    "1. Top-Rated Movies",
    "2. Most Popular Genres",
    "3. Recommend Movies (Similar Users)",
    "4. User Behavior Patterns",
    "5. Detect Trending Movies"
])

# --- Logic for Features ---

if feature == "1. Top-Rated Movies":
    st.header("⭐ Top-Rated Movies")
    st.write("Displays movies with an average rating of 4.0 or higher.")
    
    db = get_db()
    cursor = db.cursor()
    query = """
    SELECT m.title, m.genre, AVG(r.rating) as avg_rating
    FROM Movies m
    JOIN Ratings r ON m.movie_id = r.movie_id
    GROUP BY m.title, m.genre
    HAVING avg_rating >= 4.0
    ORDER BY avg_rating DESC;
    """
    cursor.execute(query)
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=['Movie Title', 'Genre', 'Average Rating'])
    st.table(df)
    db.close()

elif feature == "2. Most Popular Genres":
    st.header("📊 Most Popular Genres")
    st.write("Identifies genres based on total watch frequency.")
    
    db = get_db()
    cursor = db.cursor()
    query = """
    SELECT m.genre, COUNT(wh.watch_id) as watch_count
    FROM Movies m
    JOIN Watch_History wh ON m.movie_id = wh.movie_id
    GROUP BY m.genre
    ORDER BY watch_count DESC;
    """
    cursor.execute(query)
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=['Genre', 'Total Views'])
    st.bar_chart(df.set_index('Genre'))
    st.table(df)
    db.close()

elif feature == "3. Recommend Movies (Similar Users)":
    st.header("🔍 Recommend for Similar Users")
    user_to_rec = st.selectbox("Select a User to get Recommendations:", ["Rahul", "Sneha", "Amit", "Priya", "Vikram", "Sonia"])
    
    if st.button("Generate Recommendations"):
        db = get_db()
        cursor = db.cursor()
        query = f"""
        SELECT DISTINCT m.title 
        FROM Movies m
        JOIN Ratings r ON m.movie_id = r.movie_id
        WHERE r.user_id IN (
            SELECT user_id FROM Ratings 
            WHERE movie_id IN (SELECT movie_id FROM Ratings r2 JOIN Users u ON r2.user_id = u.user_id WHERE u.name = '{user_to_rec}')
            AND user_id != (SELECT user_id FROM Users WHERE name = '{user_to_rec}')
        )
        AND m.movie_id NOT IN (SELECT movie_id FROM Watch_History wh JOIN Users u2 ON wh.user_id = u2.user_id WHERE u2.name = '{user_to_rec}');
        """
        cursor.execute(query)
        res = cursor.fetchall()
        if res:
            for row in res:
                st.success(f"Recommended: {row[0]}")
        else:
            st.info("No recommendations available for this user yet.")
        db.close()

elif feature == "4. User Behavior Patterns":
    st.header("📈 User Behavior Patterns")
    st.write("Analyzing how many movies each user has rated and their average score.")
    
    db = get_db()
    cursor = db.cursor()
    query = """
    SELECT u.name, COUNT(r.movie_id) as movies_rated, AVG(r.rating) as avg_score
    FROM Users u
    LEFT JOIN Ratings r ON u.user_id = r.user_id
    GROUP BY u.name
    ORDER BY movies_rated DESC;
    """
    cursor.execute(query)
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=['User Name', 'Movies Rated', 'Avg Rating Given'])
    st.dataframe(df)
    db.close()

elif feature == "5. Detect Trending Movies":
    st.header("🔥 Trending Movies")
    st.write("Movies with the most views in the watch history.")
    
    db = get_db()
    cursor = db.cursor()
    query = """
    SELECT m.title, COUNT(wh.watch_id) as total_views
    FROM Movies m
    JOIN Watch_History wh ON m.movie_id = wh.movie_id
    GROUP BY m.title
    ORDER BY total_views DESC
    LIMIT 5;
    """
    cursor.execute(query)
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=['Movie Title', 'Views'])
    st.table(df)
    db.close()
