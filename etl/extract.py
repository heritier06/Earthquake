import requests
from config import USGS_URL

def fetch_earthquake_data():
    response = requests.get(USGS_URL)
    return response.json()