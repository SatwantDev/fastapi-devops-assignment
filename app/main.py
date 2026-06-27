from fastapi import FastAPI
from app.routers import auth
from app.routers import notes

app = FastAPI(
    title="AI Notes API"
)

# Register routers
app.include_router(auth.router)
app.include_router(notes.router)


@app.get("/")
def home():
    return {"message": "API Running"}


@app.get("/health")
def health():
    return {"status": "healthy"}