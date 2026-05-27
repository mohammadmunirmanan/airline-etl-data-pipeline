import pandas as pd
import sqlite3

# Load cleaned data
df = pd.read_csv('../data/cleaned_airline_bookings.csv')

# Create SQLite database
conn = sqlite3.connect('airline_pipeline.db')

# Load data into database
df.to_sql('bookings', conn, if_exists='replace', index=False)

print("Data loaded into database successfully")
