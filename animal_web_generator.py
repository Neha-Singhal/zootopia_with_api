import data_fetcher
def  generate_website(animal_name):
    """Generate an HTML page with the animal's data."""
    # Fetch data using the data fetcher
    data = data_fetcher.fetch_data(animal_name)
    if not data:
        print(f"No data found for {animal_name}.")
        return

    # Generate the website (replace this with your actual website generation logic)
    print(f"Generating website for {animal_name}...")
    for animal in data:
        print(f"Name: {animal.get('name')}")
        print(f"Taxonomy: {animal.get('taxonomy')}")
        print(f"locations: {animal.get('locations')}")
        print(f"Characteristics: {animal.get('characteristics')}")
        print("-" * 40)


def main():
    # Get user input
    animal_name = input("Please enter an animal: ")
    generate_website(animal_name)


if __name__ == "__main__":
    main()
