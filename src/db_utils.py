import sqlite3
import pandas as pd
from sqlite3 import enable_callback_tracebacks


def create_connection(db_file):
    """create a database connection to a SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to SQLite: {db_file}")
    except Error as e:
        print(f"Error: {e}")
    return conn    


def load_df_to_sql(df, table_name, conn):
    """Write records stored in a DataFrame to a SQL database"""
    try:
        # if_exists='replace' means if the table already exists, delete it and make a new one
        # index=False means don't save the row numbers (0, 1, 2...) as a column
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        print(f"Successfully loaded '{table_name}' with {len(df)} rows.")
    except ValueError as e:
        print(f"Error loading {table_name}: {e}")