import sqlite3

DB_NAME = "data.db"

# Dummy embed function to replace sentence-transformers model.encode()
def dummy_embed(texts):
    return [[0.0]*384 for _ in texts]

def create_table():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS qa_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            answer TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_qa(question, answer):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('INSERT INTO qa_data (question, answer) VALUES (?, ?)', (question, answer))
    conn.commit()
    conn.close()

def get_answer(question):
    # For now just a dummy fetch, no real embedding search
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT answer FROM qa_data WHERE question=?', (question,))
    result = c.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        return "No answer found in DB (dummy mode)."

def main():
    create_table()

    # Example insert (only run once)
    # insert_qa("What is AI?", "AI is Artificial Intelligence.")

    question = input("Enter your question: ")
    answer = get_answer(question)
    print("Answer:", answer)

if __name__ == "__main__":
    main()
