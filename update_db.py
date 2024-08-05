import pandas as pd
import sqlite3

def add_companies_from_csv(csv_file_path, db_file_path):
    # Read the CSV file
    df = pd.read_csv(csv_file_path)
    
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()
    
    # Create the companies table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS companies (
        id INTEGER PRIMARY KEY,
        name TEXT,
        category TEXT,
        subcategory TEXT
    )
    ''')
    
    # Insert data from the DataFrame into the database
    for _, row in df.iterrows():
        cursor.execute('''
        INSERT INTO companies (name, category, subcategory)
        VALUES (?, ?, ?)
        ''', (row['name'], row['topics'], row['topics']))
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    
    print(f"Successfully added {len(df)} companies to the database.")

# Usage
data_path = "datasets\product_hunt_data\phunt_startups\posts.csv"
db_file_path = "market_map.db"
add_companies_from_csv(data_path, db_file_path)

data_path_col = "datasets\product_hunt_data\phunt_startups\collections.csv"
db_file_path = "market_map.db"
add_companies_from_csv(data_path_col, db_file_path)