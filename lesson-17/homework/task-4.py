import pandas as pd

def pipeline_titanic():
    def filter_survived(df):
        return df[df['Survived'] == 1]

    def fill_missing_age(df):
        df['Age'] = df['Age'].fillna(df['Age'].mean())
        return df

    def add_fare_per_age(df):
        df['Fare_Per_Age'] = df['Fare'] / df['Age']
        return df

    titanic = pd.read_csv('titanic.csv')
    result = (titanic
              .pipe(filter_survived)
              .pipe(fill_missing_age)
              .pipe(add_fare_per_age))
    return result[['PassengerId', 'Survived', 'Age', 'Fare', 'Fare_Per_Age']]

def pipeline_flights():
    def filter_departure_delay(df):
        return df[df['DepDelay'] > 30]

    def add_delay_per_hour(df):
        df['Delay_Per_Hour'] = df['DepDelay'] / (df['AirTime'] / 60)
        return df

    flights = pd.read_parquet('flights/')
    result = (flights
              .pipe(filter_departure_delay)
              .pipe(add_delay_per_hour))
    return result[['FlightNum', 'DepDelay', 'AirTime', 'Delay_Per_Hour']]

if __name__ == "__main__":
    print("Pipeline on Titanic:")
    print(pipeline_titanic().head())

    # Flights Pipeline
    print("\nPipeline on Flights:")
    print(pipeline_flights().head())