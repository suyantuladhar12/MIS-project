
import requests
import pandas as pd
import os


def fetch_weather(city_name, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        try:
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            description = data['weather'][0]['description']

            print(f"City: {city_name}")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Weather Description: {description}")

            weather_data = {
                'City': city_name,
                'Temperature': temperature,
                'Humidity': humidity,
                'Description': description
            }
            return weather_data
        except (KeyError, IndexError) as e:
            print(f"Error: Invalid data received from the API. {e}")
            return None
    else:
        print(f"Error: Failed to fetch weather data. Status code: {response.status_code}")
        return None


if __name__ == "__main__":
    city_name = input("Enter city name: ")
    api_key = ""  # Enter your actual API key
    weather_info = fetch_weather(city_name, api_key)

    if weather_info:
        df = pd.DataFrame([weather_info])
        csv_file_path = './weather_data.csv'

        if not os.path.isfile(csv_file_path):
            df.to_csv(csv_file_path, index=False)
        else:
            df.to_csv(csv_file_path, mode='a', header=False, index=False)
        print(f"Weather data saved to {csv_file_path}")
        print(df)