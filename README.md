#### Installing
pip install sqlalchemy
pip install pymysql

By default, MySQL closes connections idle for more than eight
hours. To work around this issue, use pool_recycle=3600

from sqlalchemy import create_engine
engine = create_engine("postgresql+psycopg2://postgres:eldorado@localhost:5432/dvdrental", echo=True)
connection = engine.connect()


SQLAlchemy Core

In order to provide access to the underlying database, SQLAlchemy needs a represen‐
tation of the tables that should be present in the database. We can do this in one of
three ways:
• Using user-defined Table objects
• Using declarative classes that represent your tables
• Inferring them from the database

Types
There are four categories of types we can use inside of SQLAlchemy:
• Generic
• SQL standard
• Vendor specific
• User defined

Table 1-1. Generic type representations
SQLAlchemy 		Python 							SQL
-------------------------------------------------------------
BigInteger 		int 								BIGINT
Boolean 			bool 								BOOLEAN or SMALLINT
Date 					datetime.date 			DATE (SQLite: STRING)
DateTime 			datetime.datetime 	DATETIME (SQLite: STRING)
Enum 					str 								ENUM or VARCHAR
Float 				float or Decimal 		FLOAT or REAL
Integer 			int 								INTEGER
Interval 			datetime.timedelta 	INTERVAL or DATE from epoch
LargeBinary 	byte 								BLOB or BYTEA
Numeric 			decimal.Decimal 		NUMERIC or DECIMAL
Unicode 			unicode 						UNICODE or VARCHAR
Text 					str 								CLOB or TEXT
Time 					datetime.time 			DATETIME



