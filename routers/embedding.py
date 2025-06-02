from fastapi import APIRouter, HTTPException
from sentence_transformers import SentenceTransformer

router = APIRouter()

@router.post("/")
async def create_embedding(data: dict):
    """
    Create an embedding from the provided data.
    
    Args:
        data (dict): The input data for creating an embedding.
        
    Returns:
        dict: A dictionary containing the embedding.
    """
    # Placeholder for embedding creation logic
    # In a real application, you would integrate with an embedding model here
    sentences = ["This is an example sentence", "Each sentence is converted"]

    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    embeddings = model.encode(sentences)
    print(embeddings)

    if not data:
        raise HTTPException(status_code=400, detail="No data provided")
    
    # Simulate embedding creation
    embedding = {"embedding": embeddings.tolist()}  # Convert numpy array to list for JSON serialization

    if not embedding:
        raise HTTPException(status_code=500, detail="Failed to create embedding")
    
    # Return the created embedding
    return embedding