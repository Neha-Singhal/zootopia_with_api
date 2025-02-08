import requests

api_url = "https://api.api-ninjas.com/v1/animals"
API_KEY = "0lz6cbsgd3QHuPXoaEPYiw==vIt0EAkVAYIUuOqU"


def fetch_animal_data(animal_name):
    """Fetch animal data from the API based on user input."""
    try:
        #make API request
        headers = {'X-Api-key': API_KEY}
        params = {'name': animal_name}
        response = requests.get(api_url, headers=headers, params=params)
        response.raise_for_status() #raise an error for bad status codes
        data = response.json()
        if data:
            return{"animals":data}
        else:
            return {"animals":[]}

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
