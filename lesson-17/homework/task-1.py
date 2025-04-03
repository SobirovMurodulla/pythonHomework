import pandas as pd
import sqlite3

def inner_join_chinook():
    conn = sqlite3.connect('chinook.db')
    customers = pd.read_sql_query("SELECT * FROM customers", conn)
    invoices = pd.read_sql_query("SELECT * FROM invoices", conn)
    merged_data = pd.merge(customers, invoices, on='CustomerId', how='inner')
    total_invoices = merged_data.groupby('CustomerId').size()
    conn.close()
    return total_invoices

def outer_join_movies():
    movies = pd.read_csv('movie.csv')
    df1 = movies[['director_name', 'color']]
    df2 = movies[['director_name', 'num_critic_for_reviews']]
    left_join = pd.merge(df1, df2, on='director_name', how='left')
    full_outer_join = pd.merge(df1, df2, on='director_name', how='outer')
    left_join_count = len(left_join)
    full_outer_join_count = len(full_outer_join)
    return left_join_count, full_outer_join_count
if __name__ == "__main__":
    print("Total Invoices per Customer:")
    print(inner_join_chinook())
    
    left_count, outer_count = outer_join_movies()
    print(f"\nRows in Left Join: {left_count}")
    print(f"Rows in Full Outer Join: {outer_count}")