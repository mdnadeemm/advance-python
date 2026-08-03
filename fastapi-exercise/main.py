from fastapi import FastAPI
from pydantic import BaseModel
app  = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI"}

#path variable
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

# terminal command to start
# uvicorn main:app --reload

@app.get("/health")
def health_check():
    return {"status": "ok"}


# using query parameters
@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

# post using pydantic to get json convert it into User object validate type passes to create_user function
@app.post("/users/")
def create_user(user: User):
    return user



# usign this model to responce this fields to client
class Item(BaseModel):
    name: str
    price: float
    in_stock: bool

@app.get("/item/", response_model=Item)
def get_item():
    return {"name": "Pen", "price": 2.5, "in_stock": True}


""" validating request body and response body like Dto"""
class UserCreateDto(BaseModel):
    name: str
    email: str

class UserResponseDto(BaseModel):
    id: int
    name: str
    email: str

@app.post("/user/", response_model=UserResponseDto)
def user(request: UserCreateDto):
    created_user = {"id": 1, "name": request.name, "email": request.email}
    return created_user


@app.put("/users/{user_id}/items/")
def update_item(user_id: int, q: str | None = None, item: Item = None):
    return {"user_id": user_id, "q": q, "item": item}
