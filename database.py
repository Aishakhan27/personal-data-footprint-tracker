from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:masood@localhost:5432/footprint_tracker"

engine = create_engine(DATABASE_URL)