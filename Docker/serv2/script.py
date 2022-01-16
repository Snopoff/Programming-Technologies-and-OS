#!/usr/bin/env python3
import pandas as pd
from sqlalchemy import create_engine
import time
import sys
import os

username = os.environ['MYSQL_USER']
password = os.environ['MYSQL_PASSWORD']
host = os.environ['MYSQL_HOST']
db = os.environ['MYSQL_DATABASE']

df = pd.read_csv('data.csv', header=None)

connection_str = 'mysql+mysqlconnector://{}:{}@{}:3306/{}'.format(
    username, password, host, db)

time.sleep(30)

engine = create_engine(connection_str)
connection = engine.connect()

df.to_sql(name='sample_table2', con=connection)
sys.stdout.write(str(connection.execute(
    'SELECT * FROM sample_table2;').fetchall()))
