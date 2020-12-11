import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# user = os.environ['POSTGRES_USER']
# password = os.environ['POSTGRES_PASSWORD']
# database = os.environ['POSTGRES_DB']
# host = os.environ['POSTGRES_HOST']
# port = os.environ['POSTGRES_PORT']


user = 'admin'
password = 'api-db'
database = 'feira-livre'
host = 'feira-livre-db'
port = 5432

DATABASE_CONNECTION_URI = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'
engine = db.create_engine(DATABASE_CONNECTION_URI)

Base = declarative_base()

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
