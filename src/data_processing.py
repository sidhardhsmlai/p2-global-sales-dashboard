import pandas as pd
import sys
import os

# Ensure we can import db_utils from the same directory
try:
    import db_utils
except ImportError:
    from src import db_utils

def load_sql_query(query_name):
    """
    Reads a SQL file from the sql_queries folder.
    Uses ABSOLUTE paths to ensure it works from notebooks or terminal.
    """
    # 1. Get the directory where THIS script (data_processing.py) lives
    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 2. Go up one level to the Project Root
    project_root = os.path.dirname(current_script_dir)
    
    # 3. Build the path to the SQL file
    file_path = os.path.join(project_root, 'sql_queries', f'{query_name}.sql')
    
    # Debug print (optional, helps verify path)
    # print(f"DEBUG: Loading SQL from {file_path}")

    with open(file_path, 'r') as file:
        return file.read()

def get_data(db_path=None):
    """
    Orchestrates the entire data loading process.
    """
    # Handle DB Path Robustly
    if db_path is None:
        # Default to standard location relative to project root
        current_script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(current_script_dir)
        db_path = os.path.join(project_root, 'data', 'superstore.db')

    # 1. Connect to the Vault
    conn = db_utils.create_connection(db_path)
    if not conn:
        return None
    
    data_dict = {}
    
    try:
        # 2. Run Queries
        print("Loading YoY Growth...")
        sql_growth = load_sql_query('query_growth')
        data_dict['growth'] = pd.read_sql_query(sql_growth, conn)
        
        print("Loading Contribution...")
        sql_contrib = load_sql_query('query_contribution')
        data_dict['contribution'] = pd.read_sql_query(sql_contrib, conn)
        
        print("Loading Returns...")
        sql_returns = load_sql_query('query_returns')
        data_dict['returns'] = pd.read_sql_query(sql_returns, conn)
        
        print("Loading Managers...")
        sql_managers = load_sql_query('query_managers')
        data_dict['managers'] = pd.read_sql_query(sql_managers, conn)
        
        print("✅ All data loaded successfully.")
        
    except Exception as e:
        print(f"❌ Error executing queries: {e}")
        return None
    finally:
        conn.close()
        
    return data_dict

if __name__ == "__main__":
    data = get_data()
    if data:
        print("\n--- Data Check: Growth Table Head ---")
        print(data['growth'].head())