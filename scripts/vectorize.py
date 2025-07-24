import sqlite3
import faiss
import openai
import os
import json
import numpy as np
from dotenv import load_dotenv
from tqdm import tqdm  # Progress bar while looping

# Load your OpenAI API key from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Toggle this to True to skip OpenAI API calls and generate random embeddings for testing
USE_MOCK = True

# Connect to the local SQLite database
conn = sqlite3.connect("data/products.db")
cursor = conn.cursor()

# Query products: we combine title + description for better context
cursor.execute("SELECT id, title, description FROM products")
rows = cursor.fetchall()

# Prepare data for embedding
product_ids = []
product_texts = []

for row in rows:
    pid, title, desc = row
    product_ids.append(pid)
    product_texts.append(f"{title}\n{desc}")  # Combine title & description

# Create OpenAI embeddings using text-embedding-3-small (cheap + good)
def get_embedding(text):
    if USE_MOCK:
        # Generate random vector of size 1536 (typical OpenAI embedding size)
        return np.random.rand(1536).tolist()
    try:
        response = openai.embeddings.create(
            model="text-embedding-3-small",
            input=text
        )
        return response.data[0].embedding
    except Exception as e:
        print(f"Embedding failed: {e}")
        return None

# Generate embeddings for all products
print("Generating embeddings...")
embeddings = []
valid_ids = []

for pid, text in tqdm(zip(product_ids, product_texts), total=len(product_texts)):
    emb = get_embedding(text)
    if emb:
        embeddings.append(emb)
        valid_ids.append(pid)

if not embeddings:
    print("No embeddings generated. Please check your OpenAI API key and quota.")
    exit(1)

# Convert to FAISS format
dimension = len(embeddings[0])  # e.g. 1536 for OpenAI
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings).astype("float32"))

# Save index and metadata (ID mapping)
faiss.write_index(index, "data/products.index")

with open("data/id_map.json", "w") as f:
    json.dump(valid_ids, f)

print("✅ FAISS index and ID map saved.")
