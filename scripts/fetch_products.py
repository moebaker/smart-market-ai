import requests  # Library to send HTTP requests (get data from websites)
import json      # Library to work with JSON data (a common data format)

# URL of the FakeStoreAPI that returns product data
FAKESTORE_API_URL = "https://fakestoreapi.com/products"

# Function to fetch all product data from the API
def fetch_products():
    # Send a GET request to the API URL
    response = requests.get(FAKESTORE_API_URL)
    
    # Check if the request was successful (status code 200)
    response.raise_for_status()
    
    # Convert the response JSON data into Python objects (list of dicts)
    products = response.json()
    
    # Return the list of products
    return products

# Function to clean and extract only useful product fields
def clean_product_data(products):
    cleaned = []  # Create an empty list to store cleaned product info
    
    # Loop through each product dictionary in the products list
    for p in products:
        # Extract only id, title, description, price, and category
        cleaned.append({
            "id": p.get("id"),                # Unique product ID
            "title": p.get("title"),          # Product title/name
            "description": p.get("description"),  # Product description text
            "price": p.get("price"),          # Price of the product
            "category": p.get("category")     # Product category name
        })
    
    # Return the list of cleaned product dictionaries
    return cleaned

# Function to save cleaned data into a JSON file
def save_to_json(data, filename="data/cleaned_products.json"):
    # Open (or create) the file in write mode
    with open(filename, "w") as f:
        # Write the Python data into the file in JSON format, pretty-printed
        json.dump(data, f, indent=2)
    
    # Print confirmation that the file was saved
    print(f"Saved cleaned data to {filename}")

# Main function that runs the entire workflow
def main():
    # Step 1: Fetch raw product data from the API
    products = fetch_products()
    
    # Step 2: Clean the data to keep only relevant fields
    cleaned = clean_product_data(products)
    
    # Step 3: Print first 3 cleaned products to the console for inspection
    print("Sample cleaned product data:")
    for p in cleaned[:3]:
        print(p)
    
    # Step 4: Save the cleaned product data to a JSON file for future use
    save_to_json(cleaned)

# This line means "run the main() function if this file is executed directly"
if __name__ == "__main__":
    main()
