# SmartMarket AI Sync

An intelligent eCommerce product ingestion and Q&A system that automates syncing product data, enables natural language queries, and provides real-time insights through a dashboard.

---

## Features

- Pulls product data from FakeStoreAPI and cleans metadata
- Stores product information in a structured SQLite database
- Uses OpenAI embeddings and FAISS for fast, semantically relevant vector search
- Implements a LangChain-powered Q&A agent for natural language product queries (Retrieval-Augmented Generation)
- Streamlit dashboard for monitoring sync status, viewing insights, and interacting with the AI agent

---

## Tech Stack

- Python
- LangChain
- OpenAI API
- FAISS (vector search)
- SQLite
- Streamlit (dashboard/UI)

---

## Getting Started

1. Clone the repo:
   ```bash
   git clone https://github.com/moebaker/smart-market-ai.git
   cd smart-market-ai
# SmartMarket AI Sync

An intelligent eCommerce product ingestion and Q&A system that automates syncing product data, enables natural language queries, and provides real-time insights through a dashboard.

---

## Features

- Pulls product data from FakeStoreAPI and cleans metadata
- Stores product information in a structured SQLite database
- Uses OpenAI embeddings and FAISS for fast, semantically relevant vector search
- Implements a LangChain-powered Q&A agent for natural language product queries (Retrieval-Augmented Generation)
- Streamlit dashboard for monitoring sync status, viewing insights, and interacting with the AI agent

---

## Tech Stack

- Python
- LangChain
- OpenAI API
- FAISS (vector search)
- SQLite
- Streamlit (dashboard/UI)

---

## Getting Started

1. Clone the repo:
   ```bash
   git clone https://github.com/moebaker/smart-market-ai.git
   cd smart-market-ai
2. Create and activate a virtual environment:
  ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
