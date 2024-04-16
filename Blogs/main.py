from fastapi import FastAPI
from app.api.blogs import blogs_router

app = FastAPI(
    title="Basic blog CURD operations"
)

app.include_router(blogs_router)