# Movie Recommendation and Rating Analysis System

## 📌 Project Overview
This project is a database-driven application. It focuses on storing user movie ratings and analyzing that data to provide meaningful insights and recommendations. The system uses a **MySQL** backend for data management and a **Python (Streamlit)** frontend for the user interface.

## 📂 Project Structure
To keep the project organized and professional, the SQL logic is divided into three parts:
* `schema_design.sql`: Defines the database tables and relationships (Foreign Keys).
* `insert_data.sql`: Populates the tables with 20+ records of users, movies, and ratings.
* `analysis_queries.sql`: Contains the core SQL logic for all analytical tasks.
* `app.py`: The Python script that runs the interactive dashboard.

## 🚀 Key Features & Functionalities
The system performs the following 5 key tasks as per the project requirements:
1. **Top-Rated Movies**: Identifies movies with an average rating of 4.0 or higher.
2. **Popular Genres**: Calculates which movie genres are watched the most.
3. **Recommendation Engine**: Suggests new movies to a user based on the tastes of similar users.
4. **User Behavior Patterns**: Analyzes how many ratings each user has submitted.
5. **Trending Movies**: Detects the most frequently watched movies in recent history.

## 🛠️ Tech Stack
* **Database**: MySQL (Relational Database)
* **Programming**: Python 
* **Libraries**: `streamlit`, `mysql-connector-python`, `pandas`
* **Tools**: MySQL Workbench, Terminal (Mac)

## 📖 Setup & Execution
1. **Database Setup**:
   - Open MySQL Workbench and run `schema_design.sql`.
   - Run `insert_data.sql` to fill the database.
   
2. **Environment Setup**:
   - Install the required Python libraries:
     ```bash
     pip install streamlit mysql-connector-python pandas
     ```

3. **Running the UI**:
   - Navigate to the project folder in Terminal.
   - Run the command:
     ```bash
     streamlit run app.py
     ```
   - Use the **Checkboxes/Radio buttons** in the app to navigate through the different analytical views.
