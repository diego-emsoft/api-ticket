from fastapi import FastAPI
from app.api.v1.routes import status
from app.database.session import engine, Base

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


app.include_router(status.router, prefix="/api/v1/status", tags=["status"])

Base.metadata.create_all(bind=engine)
