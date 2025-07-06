from fastapi import FastAPI
from yacine.routes import router

app = FastAPI()
app.include_router(router)
