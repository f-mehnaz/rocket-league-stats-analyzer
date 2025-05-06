from sqlalchemy import Column, Integer, String, Float, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


Base = declarative_base()

class PlayerStats(Base):
    __tablename__ = 'player_stats'

    id = Column(Integer, primary_key=True)
    player = Column(String)
    goals = Column(Integer)
    assists = Column(Integer)
    wins = Column(Integer)
    boost_usage = Column(Float)
    match_date = Column(Date)

engine = create_engine("sqlite:///stats.db")

Base.metadata.create_all(engine)