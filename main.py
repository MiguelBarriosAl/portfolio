from fastapi import FastAPI

from api.endpoints import router as ask_router

app = FastAPI()
app.include_router(ask_router)
