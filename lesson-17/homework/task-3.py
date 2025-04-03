import pandas as pd


def classify_age_group(row):
    return 'Child' if row < 18 else 'Adult'

def apply_custom_function_titanic():
    titanic = pd.read_csv('titanic.csv')

    titanic['Age_Group'] = titanic['Age'].apply(classify_age_group)
    return titanic[['PassengerId', 'Age', 'Age_Group']]

def normalize_salaries():
    employees = pd.read_csv('employee.csv')
    employees['Normalized_Salary'] = employees.groupby('Department')['Salary'].transform(
        lambda x: (x - x.min()) / (x.max() - x.min())
    )
    return employees[['EmployeeID', 'Department', 'Salary', 'Normalized_Salary']]

def classify_movie_duration(duration):
    if duration < 60:
        return 'Short'
    elif 60 <= duration <= 120:
        return 'Medium'
    else:
        return 'Long'

def apply_custom_function_movies():
    movies = pd.read_csv('movie.csv')
    movies['Duration_Category'] = movies['duration'].apply(classify_movie_duration)
    return movies[['movie_title', 'duration', 'Duration_Category']]

if __name__ == "__main__":
    print("Titanic Age Group Classification:")
    print(apply_custom_function_titanic().head())
    
  
    print("\nNormalized Employee Salaries:")
    print(normalize_salaries().head())
    
    print("\nMovie Duration Classification:")
    print(apply_custom_function_movies().head())