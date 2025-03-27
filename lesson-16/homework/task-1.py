import pandas as pd
import sqlite3

conn = sqlite3.connect('chinook.db') 
customers_df = pd.read_sql_query("SELECT * FROM customers", conn)
print("First 10 rows of the customers table:")
print(customers_df.head(10))
conn.close()

iris_df = pd.read_json('iris.json')
print("\nShape of the iris dataset:", iris_df.shape)
print("Column names in the iris dataset:", iris_df.columns.tolist())

titanic_df = pd.read_excel('titanic.xlsx')
print("\nFirst 5 rows of the Titanic dataset:")
print(titanic_df.head())

flights_df = pd.read_parquet('flights.parquet')
print("\nSummary of the Flights dataset:")
print(flights_df.info())

movie_df = pd.read_csv('movie.csv')
print("\nRandom sample of 10 rows from the movie dataset:")
print(movie_df.sample(10))