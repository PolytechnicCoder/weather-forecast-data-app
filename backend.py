import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
def get_data(place, forecast_days=None):
   url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
   response = requests.get(url)
   data = response.json()
   filterd_data = data["list"]
   nr_values = 8 * forecast_days
   filterd_data = filterd_data[:nr_values]
   return filterd_data


if __name__ == "__main__":
   print(get_data(place="Tokyo", forecast_days=3))