from data_fetcher import fetch_animal_data

def  generate_website(animal_name, data):
    """Generate an HTML page with the animal's data."""
    filename = "animals.html"

    with open(filename ,"w") as file:
            file.write("<html><head><title>Animal Info</title></head><body>")
            file.write(f"<h1> search Results for: {animal_name}</h1>")

            if data and "animals" in data and data["animals"]:
                for animal in data["animals"]:  # Adjust based on API response structure
                    file.write(f"<h2>{animal['name']}</h2>")
                    file.write(f"<p>{animal.get('characteristics', 'no description available')}</p>")
            else:
                file.write(f"<h2>The animal '{animal_name}' doesn't exist.</h2>")
            file.write("</body></html>")
    print(f"Website generated successfully as {filename}!")

animal_name = input("Enter a name of animal:")
data = fetch_animal_data(animal_name) #Fetch data from API

generate_website(animal_name,data)  #Generate website based on API data



