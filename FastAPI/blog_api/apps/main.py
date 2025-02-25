from fastapi import FastAPI

from apps.database import Base, engine
from apps.routes import blog, user

app = FastAPI()

# Include blog and user routes
app.include_router(blog.router, prefix="/blogs", tags=["Blogs"])
app.include_router(user.router, prefix="/users", tags=["Users"])


@app.get("/", tags=["Entry Point"])
def root():
    return {"message": "Welcome to Blog API"}
