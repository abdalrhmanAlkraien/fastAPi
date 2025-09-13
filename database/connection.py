from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_CONNECTION_STRING = "postgresql+psycopg2://username:password@localhost:3306/book_db"
engine = create_engine(DATABASE_CONNECTION_STRING, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()