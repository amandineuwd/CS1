from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from typing import List
import uuid

app = FastAPI()

# Configure CORS to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify the exact origin
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve the frontend
@app.get("/", response_class=HTMLResponse)
def get_index():
    with open('index.html', 'r') as file:
        return file.read()

# Predefined valid username and password
VALID_USERNAME = "createch"
VALID_PASSWORD = "root"

class Login(BaseModel):
    username: str
    password: str

@app.post('/login', status_code=200)
def login(login: Login):
    # Check if the username and password match
    if login.username == VALID_USERNAME and login.password == VALID_PASSWORD:
        return {"message": "Login successful"}
    raise HTTPException(status_code=401, detail="Invalid username or password")

# --------------------------
# Post-it Note Models
# --------------------------

class PostItBase(BaseModel):
    text: str
    style: dict  # e.g., {"top": "100px", "left": "150px"}

class PostItCreate(PostItBase):
    pass

class PostIt(PostItBase):
    id: str

# In-memory storage for Post-it notes
postits: List[PostIt] = []

@app.get("/postits", response_model=List[PostIt])
def get_postits():
    return postits

@app.post("/postits", response_model=PostIt, status_code=201)
def add_postit(postit: PostItCreate):
    new_postit = PostIt(id=str(uuid.uuid4()), **postit.dict())
    postits.append(new_postit)
    return new_postit

@app.delete("/postits/{postit_id}", status_code=204)
def delete_postit(postit_id: str):
    global postits
    original_length = len(postits)
    postits = [p for p in postits if p.id != postit_id]
    if len(postits) == original_length:
        raise HTTPException(status_code=404, detail="Post-it not found")
    return

# --------------------------
# Additional Endpoints for Other Categories
# --------------------------

# Similar endpoints can be created for Secrets, Tasks, etc.
# For brevity, only Post-it notes are handled here.

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000, reload=True)
