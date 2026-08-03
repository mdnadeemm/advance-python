from fastapi import FastAPI
app  = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

# terminal command to start
# uvicorn main:app --reload

@app.get("/health")
def health_check():
    return {"status": "ok"}
