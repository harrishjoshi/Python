from fastapi import FastAPI

from apps.routes import auth, blog, user

app = FastAPI()

app.include_router(auth.router)
app.include_router(blog.router, prefix="/blogs", tags=["Blogs"])
app.include_router(user.router, prefix="/users", tags=["Users"])


@app.get("/", tags=["Entry Point"])
def root():
    return {"message": "Welcome to Blog API"}
