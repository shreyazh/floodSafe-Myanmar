import pandas as pd
import requests

def fetch_meteorology_data():
    url = "https://www.weatherapi.com/weather/q/rangoon-1576335" # openweathermap API can also be used 
    response = requests.get(url)
    data = response.json()  
    
    # Preprocessing and structuring the data
    weather_data = {
        "rainfall": data['rainfall'],
        "soil_humidity": data['soil_humidity'],
        "temperature": data['temperature'],
        "water_level": data['water_level']
    }
    return pd.DataFrame([weather_data])
