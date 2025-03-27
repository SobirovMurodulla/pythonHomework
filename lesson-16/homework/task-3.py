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

iris_stats = iris_df.describe().T 
iris_stats['median'] = iris_df.median() 
print("\nMean, Median, and Standard Deviation for numerical columns in the iris dataset:")
print(iris_stats[['mean', 'median', 'std']])


age_min = titanic_df['age'].min()
age_max = titanic_df['age'].max()
age_sum = titanic_df['age'].sum()
print("\nTitanic passenger age statistics:")
print(f"Minimum age: {age_min}, Maximum age: {age_max}, Sum of ages: {age_sum}")


top_director = movie_df.groupby('director_name')['director_facebook_likes'].sum().idxmax()
top_director_likes = movie_df.groupby('director_name')['director_facebook_likes'].sum().max()
print(f"\nDirector with the highest total director_facebook_likes: {top_director} ({top_director_likes} likes)")


longest_movies = movie_df.nlargest(5, 'duration')[['movie_title', 'duration', 'director_name']]
print("\n5 Longest Movies and their Directors:")
print(longest_movies)


missing_values = flights_df.isnull().sum()
print("\nMissing values in the Flights dataset:")
print(missing_values)


if 'air_time' in flights_df.columns:
    flights_df['air_time'].fillna(flights_df['air_time'].mean(), inplace=True)
    print("\nMissing values in 'air_time' column filled with mean.")