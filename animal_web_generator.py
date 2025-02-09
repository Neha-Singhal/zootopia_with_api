import data_fetcher
def  generate_website(animal_name):
    """Generate an HTML page with the animal's data."""
    # Fetch data using the data fetcher
    data = data_fetcher.fetch_data(animal_name)
    if not data:
        print(f"No data found for {animal_name}.")
        return

        # Generate HTML content
    html_content ="""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My Animal Repository</title>
        <style>
            body {
                background-color: #ffe6e6;
                font-family: Arial, sans-serif;
                text-align: center;
            }
            h1 {
                margin-top: 20px;
            }
            .container {
                width: 80%;
                margin: auto;
            }
            .card {
                background: white;
                padding: 20px;
                margin: 20px auto;
                width: 60%;
                border-radius: 10px;
                box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
                text-align: left;
            }
            .card h2 {
                text-transform: uppercase;
                font-size: 22px;
            }
            .card p {
                font-size: 16px;
                margin: 5px 0;
            }
            .bold {
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <h1>My Animal Repository</h1>
        <div class="container">
    """

    # Loop through data to create cards
    for animal in data:
        html_content += f"""
        <div class="card">
            <h2>{animal.get('name', 'Unknown')}</h2>
            <p><span class="bold">Taxonomy:</span> {animal.get('taxonomy', {})}</p>
            <p><span class="bold">Location:</span> {', '.join(animal.get('locations', []))}</p>
            <p><span class="bold">Characteristics:</span> {animal.get('characteristics', {})}</p>
        </div>
        """

    # End HTML content
    html_content += """
        </div>
    </body>
    </html>
    """

    # Save the HTML file
    with open("animals.html", "w") as file:
        file.write(html_content)

    print(f"animals.html has been generated successfully!")


def main():
    # Get user input
    animal_name = input("Please enter an animal: ")
    generate_website(animal_name)


if __name__ == "__main__":
    main()
