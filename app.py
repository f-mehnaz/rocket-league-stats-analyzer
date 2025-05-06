import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import PlayerStats

engine = create_engine('sqlite:///stats.db')
Session = sessionmaker(bind=engine)
session = Session()

player_stats = session.query(PlayerStats).all()

st.title("Rocket League Player Stats")

st.subheader("Player Stats")
data = []
for stat in player_stats:
    data.append([stat.player, stat.goals, stat.assists, stat.wins, stat.boost_usage, stat.match_date])

import pandas as pd
df = pd.DataFrame(data, columns=["Player", "Goals", "Assists", "Wins", "Boost Usage", "Match Date"])

st.write(df)

session.close()
