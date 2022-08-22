import sqlalchemy as db
import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

# 1) Connect to the database here using the SQLAlchemy's create_engine function
def connect():
    global engine # this allows us to use a global variable called engine
    # A "connection string" is basically a string that contains all the databse credentials together
    connection_string = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}?autocommit=true"
    print("Starting the connection...")
    engine = create_engine(connection_string)
    engine.connect()
    return engine
connect()

# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function
engine.execute("""
CREATE TABLE cars(
car_id INT NOT NULL,
mark VARCHAR(255) NOT NULL,
model VARCHAR(255) NOT NULL,
PRIMARY KEY(car_id)
);
""")

# 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function
engine.execute("INSERT INTO cars(car_id,mark,model) values (1,'Chevorlet','Captiva');")

# 4) Use pandas to print one of the tables as dataframes using read_sql function
df_results = pd.read_sql("Select * from cars;", engine)
print(df_results)