from flask import Flask, render_template, request, jsonify
from sentence_transformers import SentenceTransformer
from transformers import pipeline
import faiss
import numpy as np

# Sample documents - knowledge base for the chatbot
documents = [
    "The capital of France is Paris.",
    "The Great Wall of China is visible from space.",
    "Python is a popular programming language.",
    "The tallest mountain in the world is Mount Everest.",
    "The FIFA World Cup is the most prestigious football tournament.",
    "Cristiano Ronaldo is one of the greatest football players.",
    "Lionel Messi holds numerous records in football.",
    "The Premier League is one of the most watched football leagues in the world.",
    "The UEFA Champions League is contested by top football clubs across Europe.",
    "A football match lasts for 90 minutes, divided into two halves of 45 minutes."
]

# Initialize the SentenceTransformer and FAISS index
embedder = SentenceTransformer('all-MiniLM-L6-v2')
doc_embeddings = embedder.encode(documents)
dimension = doc_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(doc_embeddings))

# Initialize the question-answering pipeline
qa = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

# Initialize Flask app
app = Flask(__name__)

# Function to handle question answering
def ask_question(question):
    """
    Process the user's question, find the most relevant document, and extract an answer.
    """
    q_vector = embedder.encode([question])
    _, I = index.search(np.array(q_vector), k=1)  # Search for the most similar document
    matched_doc = documents[I[0][0]]  # Get the matched document

    # Use the Hugging Face QA model to extract an answer from the matched document
    result = qa(question=question, context=matched_doc)
    return result['answer']

# Route to display the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the chat logic (POST requests)
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if user_input:
        answer = ask_question(user_input)  # Get the answer based on the question
        return jsonify({"response": answer})
    return jsonify({"response": "Sorry, I didn't understand that."})

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
