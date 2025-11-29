import pytest
import os
import sys
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src import data_processing

def test_load_sql_query():
    """Test that we can read a SQL file correctly."""
    # We check if 'query_growth' loads and contains the word SELECT
    sql = data_processing.load_sql_query('query_growth')
    assert "SELECT" in sql
    assert "FROM" in sql

def test_get_data_structure():
    """Test that get_data returns the correct dictionary structure."""
    if os.path.exists('data/superstore.db'):
        data = data_processing.get_data('data/superstore.db')
        
        # This verifies ALL 4 tables exist in the output
        assert isinstance(data, dict)
        assert 'growth' in data
        assert 'contribution' in data
        assert 'returns' in data
        assert 'managers' in data
        
        # Verify they are not empty
        assert len(data['growth']) > 0
    else:
        pytest.skip("Database file not found.")