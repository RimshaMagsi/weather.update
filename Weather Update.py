import requests
import pandas as pd

# Replace 'YOUR_API_KEY' with your OpenWeatherMap API key
API_KEY = "YOUR_API_KEY"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Extensive list of cities in Sindh, Pakistan
sindh_cities = [
    "Karachi", "Hyderabad", "Sukkur", "Larkana", "Nawabshah",
    "Mirpur Khas", "Dadu", "Badin", "Jacobabad", "Shikarpur",
    "Thatta", "Ghotki", "Kashmore", "Khairpur", "Mithi",
    "Umerkot", "Tando Allahyar", "Tando Adam", "Kandhkot", "Kotri",
    "Sehwan", "Qambar", "Jamshoro", "Hala", "Mehar",
    "Moro", "Sanghar", "Khipro", "Matli", "Sujawal"
]

# Function to fetch weather data for a single city
def get_weather_data(city_name):
    try:
        params = {"q": city_name, "appid": API_KEY, "units": "metric"}
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise error for bad responses
        data = response.json()
        return {
            "City": city_name,
            "Temperature (°C)": data["main"]["temp"],
            "Humidity (%)": data["main"]["humidity"],
            "Weather": data["weather"][0]["description"].capitalize(),
            "Wind Speed (m/s)": data["wind"]["speed"]
        }
    except Exception as e:
        return {
            "City": city_name,
            "Temperature (°C)": "N/A",
            "Humidity (%)": "N/A",
            "Weather": "Error fetching data",
            "Wind Speed (m/s)": "N/A"
        }

# Main script to fetch and display weather data for all cities
if __name__ == "__main__":
    print("Fetching weather data for all cities in Sindh...\n")
    
    # Fetch weather data for all cities
    weather_data = [get_weather_data(city) for city in sindh_cities]
    
    # Convert the data to a DataFrame
    df = pd.DataFrame(weather_data)
    
    # Display the data
    print(df)
    
    # Save data to a CSV file
    csv_file = "sindh_weather_all_cities.csv"
    df.to_csv(csv_file, index=False)
    print(f"\nWeather data has been saved to '{csv_file}'.")
