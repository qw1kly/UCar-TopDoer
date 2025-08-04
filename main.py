from fastapi import FastAPI
import uvicorn
from routes import post, get
from fastapi.middleware.cors import CORSMiddleware
from config.database_connection import manager

app = FastAPI()

app.include_router(post.router)
app.include_router(get.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "DELETE"],
    allow_headers=["*"]
)

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0')