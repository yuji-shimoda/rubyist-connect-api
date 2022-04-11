import databases
import sqlalchemy

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(DATABASE_URL)
