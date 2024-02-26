from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# This allows only the localhost to access the backend
# (Should be changed for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080", "https://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/answer")
def get_answer():
    return {"answer": 42}