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

iris_df.columns = iris_df.columns.str.lower()
iris_selected = iris_df[['sepal_length', 'sepal_width']]
print("\nSelected columns from the iris dataset:")
print(iris_selected.head())

titanic_filtered = titanic_df[titanic_df['age'] > 30]
print("\nPassengers older than 30:")
print(titanic_filtered.head())

gender_counts = titanic_df['sex'].value_counts()
print("\nCount of male and female passengers:")
print(gender_counts)


flights_selected = flights_df[['origin', 'dest', 'carrier']]
print("\nSelected columns from the Flights dataset:")
print(flights_selected.head())

unique_destinations = flights_df['dest'].nunique()
print("\nNumber of unique destinations in the Flights dataset:", unique_destinations)


movies_filtered = movie_df[movie_df['duration'] > 120]
movies_sorted = movies_filtered.sort_values(by='director_facebook_likes', ascending=False)
print("\nMovies with duration > 120 minutes, sorted by director_facebook_likes:")
print(movies_sorted.head())