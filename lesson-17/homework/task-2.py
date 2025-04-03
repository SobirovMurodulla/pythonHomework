import pandas as pd

def grouped_aggregations_titanic():
    titanic = pd.read_csv('titanic.csv')
    grouped = titanic.groupby('Pclass').agg({
        'Age': 'mean',
        'Fare': 'sum',
        'PassengerId': 'count'
    })
    grouped.rename(columns={'Age': 'Average Age', 'Fare': 'Total Fare', 'PassengerId': 'Passenger Count'}, inplace=True)
    
    return grouped

def multi_level_grouping_movies():
    movies = pd.read_csv('movie.csv')
    grouped = movies.groupby(['color', 'director_name']).agg({
        'num_critic_for_reviews': 'sum',
        'duration': 'mean'
    })
    
    grouped.rename(columns={'num_critic_for_reviews': 'Total Critic Reviews', 'duration': 'Average Duration'}, inplace=True)
    
    return grouped

def nested_grouping_flights():
    flights = pd.read_parquet('flights/')
    
    grouped = flights.groupby(['Year', 'Month']).agg({
        'FlightNum': 'count',
        'ArrDelay': 'mean',
        'DepDelay': 'max'
    })
    
    grouped.rename(columns={'FlightNum': 'Total Flights', 'ArrDelay': 'Average Arrival Delay', 'DepDelay': 'Max Departure Delay'}, inplace=True)
    
    return grouped

if __name__ == "__main__":
    print("Grouped Aggregations on Titanic:")
    print(grouped_aggregations_titanic())
    
    print("\nMulti-level Grouping on Movie Data:")
    print(multi_level_grouping_movies())

    print("\nNested Grouping on Flights:")
    print(nested_grouping_flights())