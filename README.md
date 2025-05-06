Rocket League Stats Analyzer 

A simple Python app that analyzes Rocket League player performance data. This project uses **SQLAlchemy**, **Pandas**, and **Streamlit** to visualize player stats from a local SQLite database.

# Features

* Display **Rocket League player statistics** in a clean, tabular format
* **Visualize performance data** such as goals scored, boosts used, and other key metrics
* **SQLite database** for storing player stats
* **Mock data loading** for testing purposes

# Technologies Used

* **Python**: The main language used for data manipulation and backend logic.
* **SQLAlchemy**: ORM used to interact with the SQLite database.
* **Pandas**: Data manipulation and analysis.
* **Streamlit**: Web framework for displaying the data in a user-friendly way.
* **SQLite**: Local database for storing player stats.

# Project Structure

* `app.py`: Streamlit app to display the data in a simple table format.
* `db/`: Contains database models and the SQLite database (`stats.db`).
* `scripts/`: Contains the script for loading mock data into the database.
* `data/`: Contains sample data files.
* `requirements.txt`: List of Python dependencies.

# Database Setup

The app uses an **SQLite** database (`stats.db`) to store player stats. 
