from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Load environment variables
load_dotenv()

# Initialize the embedding model
embeddings = GoogleGenerativeAIEmbeddings( 
    model="models/gemini-embedding-001"
)

# Text to embed
text = "Generative AI is transforming software development."

# Generate embedding
vector = embeddings.embed_query(text)

print("Embedding Dimension:", len(vector))
print("\nFirst 10 Values:")
print(vector[:10])

"""
for the multiple documents
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

documents = [
    "Artificial Intelligence",
    "Machine Learning",
    "Deep Learning",
    "Generative AI"
]

vectors = embeddings.embed_documents(documents)

print(f"Total Embeddings: {len(vectors)}")
print(f"Dimensions: {len(vectors[0])}")
"""
