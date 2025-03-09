from bs4 import BeautifulSoup


with open('weather.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')


weather_data = []
rows = soup.find('tbody').find_all('tr')
for row in rows:
    day = row.find_all('td')[0].text
    temperature = int(row.find_all('td')[1].text.replace('°C', ''))
    condition = row.find_all('td')[2].text
    weather_data.append({'day': day, 'temperature': temperature, 'condition': condition})


print("Weather Data:")
for data in weather_data:
    print(f"Day: {data['day']}, Temperature: {data['temperature']}°C, Condition: {data['condition']}")


max_temp = max(weather_data, key=lambda x: x['temperature'])
print(f"\nDay with the highest temperature: {max_temp['day']} ({max_temp['temperature']}°C)")


sunny_days = [data['day'] for data in weather_data if data['condition'] == 'Sunny']
print(f"Days with 'Sunny' condition: {', '.join(sunny_days)}")


average_temp = sum(data['temperature'] for data in weather_data) / len(weather_data)
print(f"\nAverage temperature for the week: {average_temp:.2f}°C")