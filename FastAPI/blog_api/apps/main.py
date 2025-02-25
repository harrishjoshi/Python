from fastapi import FastAPI

from apps.database import Base, engine
from apps.routes import blog

app = FastAPI()

# Include blog routes
app.include_router(blog.router, prefix="/blogs", tags=["Blogs"])


@app.get("/")
def read_root():
    return {"message": "Welcome to Blog API"}
