from fastapi import FastAPI
from database import Base, engine
from routers import auth, posts

app = FastAPI()

# Include routers

app.include_router(posts.router, prefix="/api")  #routing for post related endpoints
app.include_router(auth.router, prefix="/auth")  #routing for signup, login etc.

@app.get("/")
def root():
    return "HELLO THIS IS APP"

@app.get("/createdb") #Make request to this endpoint to create Database tables
def create_db():
    Base.metadata.create_all(bind=engine)
    return "dbcreated"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)




