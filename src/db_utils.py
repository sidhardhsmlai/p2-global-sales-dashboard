import sqlite3
from sqlite3 import Error
import pandas as pd

def create_connection(db_file):
    """create a database connection to a SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(f"Error connecting to DB: {e}")
    return conn

def load_df_to_sql(df, table_name, conn):
    """Write records stored in a DataFrame to a SQL database"""
    try:
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        print(f"Successfully loaded '{table_name}' with {len(df)} rows.")
    except ValueError as e:
        print(f"Error loading {table_name}: {e}")