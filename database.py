from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://postgres:newpassword@localhost:5432/order"

# Create engine
engine = create_engine(db_url, echo=True)  # echo=True for logging SQL queries

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
