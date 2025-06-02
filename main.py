# Run with `uvicorn main:app --reload`
from fastapi import FastAPI, HTTPException
from pathlib import Path
from routers.embedding import router as embedding

app = FastAPI()

app.include_router(embedding, prefix="/embedding", tags=["embedding"])

@app.get("/")
async def root():
    return {"Hello": "World"}

@app.get("/unstructured-test")
async def unstructured_test():
    """Test endpoint for unstructured library."""
    from unstructured.partition.auto import partition

    filename = Path("docs/bert_paper.pdf")

    if not filename.exists():
        raise HTTPException(status_code=404, detail="File not found")
    else:
        elements = partition(filename=filename)
        print("\n\n".join([str(el) for el in elements]))
        return "\n\n".join([str(el) for el in elements])

@app.post("/dataframe")
async def create_dataframe(text: str = None, embedding: str = None):
    """Test endpoint for creating a DataFrame."""
    import pandas as pd

    data = {
        "name": ["Alice", "Bob", "Charlie"],
        "age": [25, 30, 35],
        "city": ["New York", "Los Angeles", "Chicago"]
    }
    
    df = pd.DataFrame(data)
    return df.to_dict(orient="records")

