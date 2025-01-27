import sqlite3
import pandas as pd

# Part 1: Reading Files

# 1. Read from chinook.db (SQLite)
conn = sqlite3.connect('chinook.db')
df_customers = pd.read_sql_query("SELECT * FROM customers", conn)
print(df_customers.head(10))
conn.close()

# 2. Load iris.json (JSON)
df_iris = pd.read_json('iris.json')
print(df_iris.shape)
print(df_iris.columns)

# 3. Load titanic.xlsx (Excel)
df_titanic = pd.read_excel('titanic.xlsx')
print(df_titanic.head())

# 4. Read Flights parquet file (Parquet)
df_flights = pd.read_parquet('Flights.parquet')
print(df_flights.info())

# 5. Load movie.csv (CSV)
df_movie = pd.read_csv('movie.csv')
print(df_movie.sample(10))

# Part 2: Exploring DataFrames

# 1. From iris.json: Rename columns and filter
df_iris.columns = df_iris.columns.str.lower()
df_iris_filtered = df_iris[['sepal_length', 'sepal_width']]
print(df_iris_filtered.head())

# 2. From titanic.xlsx: 
