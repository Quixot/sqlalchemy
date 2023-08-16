from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://postgres:eldorado@localhost:5432/sqlalchemy", echo=True)									 
connection = engine.connect()

# we can define JSON fields that we can later use with the many PostgreSQL specific JSON functions, such as a
from sqlalchemy.dialects.postgresql import JSON


# Metadata is used to tie together the database structure
from sqlalchemy import MetaData
metadata = MetaData()


from sqlalchemy import Table, Column, Integer, Numeric, String, ForeignKey

cookies = Table('cookies', metadata,
    Column('cookie_id', Integer(), primary_key=True),
    Column('cookie_name', String(50), index=True),
    Column('cookie_recipe_url', String(255)),
    Column('cookie_sku', String(55)),
    Column('quantity', Integer()),
    Column('unit_cost', Numeric(12, 2))
)


from datetime import datetime
from sqlalchemy import DateTime

users = Table('users', metadata,
 Column('user_id', Integer(), primary_key=True),
 Column('username', String(15), nullable=False, unique=True), # 1
 Column('email_address', String(255), nullable=False),
 Column('phone', String(20), nullable=False),
 Column('password', String(25), nullable=False),
 Column('created_on', DateTime(), default=datetime.now), # 2
 Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now) # 3
)

"""
1. Here we are making this column required (nullable=False) and also requiring a unique value.
2. The default sets this column to the current time if a date isn’t specified.
3. Using onupdate here will reset this column to the current time every time any part of the record is updated
"""



