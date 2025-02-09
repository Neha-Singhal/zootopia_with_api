import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv('API_URL')
API_KEY = os.getenv('API_KEY')
print("API Key:",API_KEY)
print("API_Url:",API_URL)



def fetch_data(animal_name):
    """
        Fetches the animals data for the animal 'animal_name'.
        Returns: a list of animals, each animal is a dictionary:
        {
          'name': ...,
          'taxonomy': {
            ...
          },
          'locations': [
            ...
          ],
          'characteristics': {
            ...
          }
        }
        """
    try:
        #make API request
        headers = {'X-Api-key': API_KEY}
        params = {'name': animal_name}
        response = requests.get(API_URL, headers=headers, params=params)
        response.raise_for_status() #raise an error for bad status codes
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []
