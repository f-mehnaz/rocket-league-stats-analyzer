import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import PlayerStats

# Connect to the SQLite database
engine = create_engine('sqlite:///stats.db')
Session = sessionmaker(bind=engine)
session = Session()

# Query the player stats from the database
player_stats = session.query(PlayerStats).all()

# Display title
st.title("Rocket League Player Stats")

# Create a table to display the stats
st.subheader("Player Stats")
data = []
for stat in player_stats:
    data.append([stat.player, stat.goals, stat.assists, stat.wins, stat.boost_usage, stat.match_date])

# Create a dataframe to display it in a table format
import pandas as pd
df = pd.DataFrame(data, columns=["Player", "Goals", "Assists", "Wins", "Boost Usage", "Match Date"])

# Show the dataframe in Streamlit
st.write(df)

# Close the session
session.close()
