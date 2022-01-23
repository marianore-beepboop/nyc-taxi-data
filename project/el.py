import pandas as pd

from project.cfg import PG_CFG
from project.constants import DATA_DIR
from project.helpers import get_db_uri
from sqlalchemy import create_engine


file_name = "yellow_tripdata_2021-01"

db_uri = get_db_uri(PG_CFG)
engine = create_engine(db_uri)

with open(f"{DATA_DIR}/{file_name}.csv") as f:
    df = pd.read_csv(f, sep=",", nrows=100)

df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

pd.io.sql.get_schema(df, name="yellow_taxi_data", con=engine)

df.to_sql(name="yellow_taxi_data", con=engine, if_exists="replace")
