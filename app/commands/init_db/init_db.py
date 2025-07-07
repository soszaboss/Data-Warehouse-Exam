from database.models import Base
from database.session import engine


# Initialize the database by creating all tables defined in the models
# This function is typically called once to set up the database schema.
def init_db():
    Base.metadata.create_all(bind=engine)
    print("Database initialized.")

# Command-line interface function to initialize the database
def cli():
    init_db()