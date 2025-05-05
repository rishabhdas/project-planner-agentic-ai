import os
from langchain.memory import ConversationBufferMemory, VectorStoreRetrieverMemory
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings

# Paths
FAISS_PATH = "data/faiss_index"

# === Short-Term Memory (STM) ===
stm_memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# === Long-Term Memory (LTM) ===
embedding = OllamaEmbeddings(model="llama3.2")

# Load or create FAISS index
if os.path.exists(FAISS_PATH):
    print("Loading FAISS vectorstore from disk...")
    vectorstore = FAISS.load_local(FAISS_PATH, embeddings=embedding, allow_dangerous_deserialization=True)
else:
    print("Creating new FAISS vectorstore...")
    texts = ["Initial placeholder memory context"]
    vectorstore = FAISS.from_texts(texts, embedding=embedding)
    vectorstore.save_local(FAISS_PATH)

ltm_memory = VectorStoreRetrieverMemory(retriever=vectorstore.as_retriever())

# === Utility: Save new memory after session ends ===
def save_vectorstore():
    vectorstore.save_local(FAISS_PATH)
