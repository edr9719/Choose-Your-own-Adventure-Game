from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    
)

SessionLocal = sessionmaker(autocommit= False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
#Base.metadata.create_all() tells SQLAlchemy: “Look at all my ORM models and create the tables in the database if they don’t already exist.”
def create_tables():
    Base.metadata.create_all(bind=engine)