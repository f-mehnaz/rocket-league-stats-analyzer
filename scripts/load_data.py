import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import json
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base, PlayerStats

# Step 1: Set up database connection
engine = create_engine("sqlite:///stats.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

print("Loading mock data into the database...")
# Step 2: Load JSON data
with open("data/mock_data.json") as f:
    data = json.load(f)

# Step 3: Add each record to the DB
for entry in data:
    print(f"Inserting {entry['player']} into the database...")
    stat = PlayerStats(
        player=entry["player"],
        goals=entry["goals"],
        assists=entry["assists"],
        wins=entry["wins"],
        boost_usage=entry["boost_usage"],
        match_date=datetime.strptime(entry["match_date"], "%Y-%m-%d")
    )
    session.add(stat)

# Step 4: Commit and close session
session.commit()
session.close()

print("✅ Data loaded into stats.db")
