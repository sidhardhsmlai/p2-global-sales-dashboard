import pytest
import os
import sys
import pandas as pd

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src import db_utils

def test_create_connection():
    """Test that we can create a connection to a test database."""
    # Use an in-memory database (runs in RAM, no file created)
    conn = db_utils.create_connection(":memory:")
    assert conn is not None
    conn.close()

def test_load_df_to_sql():
    """Test that we can load a dataframe into a table and read it back."""
    conn = db_utils.create_connection(":memory:")
    data = {'col1': [1, 2], 'col2': ['a', 'b']}
    df = pd.DataFrame(data)
    
    db_utils.load_df_to_sql(df, 'test_table', conn)
    
    df_read = pd.read_sql_query("SELECT * FROM test_table", conn)
    assert len(df_read) == 2
    assert df_read['col1'].iloc[0] == 1
    conn.close()
    