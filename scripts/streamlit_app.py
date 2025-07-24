import streamlit as st

# Dummy embed function to replace sentence-transformers model.encode()
def dummy_embed(texts):
    # Return a list of fixed-length zero vectors (e.g., 384 dim)
    return [[0.0]*384 for _ in texts]

# Example QA function that uses embeddings
def answer_question(question, context):
    # Just a placeholder: in real use you'd embed and search
    return "This is a dummy answer since embeddings are disabled."

def main():
    st.title("SmartMarket AI Sync - Demo (No Torch)")

    question = st.text_input("Ask a question:")
    context = st.text_area("Context / Document Text:")

    if st.button("Get Answer"):
        # Use dummy embeddings here
        question_embedding = dummy_embed([question])
        context_embedding = dummy_embed([context])

        # Get dummy answer
        answer = answer_question(question, context)

        st.write("Answer:", answer)

if __name__ == "__main__":
    main()
