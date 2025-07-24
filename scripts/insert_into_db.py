import sqlite3
import json

DB_NAME = "data/products.db"
JSON_FILE = "data/cleaned_products.json"

def create_table(conn):
    # Create the products table if not exists
    conn.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            title TEXT,
            description TEXT,
            price REAL,
            category TEXT
        );
    ''')

def insert_products(conn, products):
    # Insert product data into products table
    with conn:
        for p in products:
            conn.execute('''
                INSERT OR REPLACE INTO products (id, title, description, price, category)
                VALUES (?, ?, ?, ?, ?)
            ''', (p['id'], p['title'], p['description'], p['price'], p['category']))

def main():
    # Load cleaned product data from JSON
    with open(JSON_FILE, 'r') as f:
        products = json.load(f)

    # Connect to (or create) SQLite DB
    conn = sqlite3.connect(DB_NAME)

    # Create table if needed
    create_table(conn)

    # Insert products
    insert_products(conn, products)
    print(f"Inserted {len(products)} products into {DB_NAME}")

    # Optional: Query and print a few entries to verify
    cursor = conn.execute('SELECT * FROM products LIMIT 3')
    for row in cursor:
        print(row)

    conn.close()

if __name__ == "__main__":
    main()
