from sentence_transformers import SentenceTransformer
from transformers import pipeline
import faiss
import numpy as np

# Sample documents - these are the knowledge base the chatbot will reference
documents = [
    "The capital of France is Paris.",
    "The Great Wall of China is visible from space.",
    "Python is a popular programming language.",
    "The tallest mountain in the world is Mount Everest."
]

# Step 1: Load the Sentence Transformer model
# The model is used to convert text (documents and questions) into vector embeddings.
embedder = SentenceTransformer('all-MiniLM-L6-v2')  # A small, fast model for generating embeddings

# Step 2: Convert documents to vector embeddings
# We encode all documents into their respective vector representations.
doc_embeddings = embedder.encode(documents)

# Step 3: Create FAISS index for efficient similarity search
# FAISS helps with efficient nearest neighbor search by storing and indexing document embeddings.
dimension = doc_embeddings.shape[1]  # The number of dimensions in the embeddings
index = faiss.IndexFlatL2(dimension)  # Using L2 (Euclidean) distance metric for similarity search
index.add(np.array(doc_embeddings))  # Add document embeddings to the index

# Step 4: Define QnA function to answer questions
def ask_question(question):
    """
    Function to process a question, find the most relevant document from the knowledge base,
    and then extract an answer using a pre-trained question-answering model.
    
    Args:
    - question (str): The question asked by the user.
    
    Returns:
    - (str): The answer extracted from the most relevant document.
    """
    # Convert the user's question into a vector embedding
    q_vector = embedder.encode([question])

    # Search for the most similar document in the FAISS index (k=1 to return the closest match)
    _, I = index.search(np.array(q_vector), k=1)
    matched_doc = documents[I[0][0]]  # Get the most relevant document based on the index result

    # Use Hugging Face's pre-trained question-answering model to extract an answer from the matched document
    qa = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
    result = qa(question=question, context=matched_doc)  # Extract the answer based on context

    # Return the extracted answer
    return result['answer']

# Step 5: Interactive QnA loop
# This allows the user to ask multiple questions in a session.
while True:
    question = input("\nAsk something (or type 'exit' to quit): ")
    
    # Exit condition
    if question.lower() == 'exit':
        print("Exiting... Goodbye!")
        break
    
    # Process the question and get the answer
    answer = ask_question(question)
    
    # Display the answer
    print("Answer:", answer)
