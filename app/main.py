from fastapi import FastAPI
from app.api import music, users

app = FastAPI()

app.include_router(music.router)
app.include_router(users.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to TCH Music Generation Platform API"}