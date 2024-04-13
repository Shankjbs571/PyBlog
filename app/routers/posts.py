from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from .auth import get_current_user
from database import engine, SessionLocal
from models import Post, User
from schemas import PostCreate, Post as PostSchema
from cachetools import TTLCache, cached

router = APIRouter()


# Create a cache with a TTL (time-to-live) of 5 minutes
cache = TTLCache(maxsize=100, ttl=300)


@router.get("/")
def root():
    return "HELLO THIS IS API"

# To create a Post token is required 
@router.post("/posts/",response_model=PostSchema )
def create_post(post: PostCreate, current_user = Depends(get_current_user)):
    # print("this si current_user", current_user)
    if len(post.text.encode('utf-8')) > 1048576:  # Convert text to bytes and check size
        raise HTTPException(status_code=413, detail="Payload size exceeds limit")
    db = SessionLocal()
    user = db.query(User).filter(User.email == current_user).first()
    db_post = Post(**post.model_dump(),owner_id=user.id)
    
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    db.close()
    return db_post

@router.get("/posts/")
@cached(cache)
def read_post(current_user = Depends(get_current_user)):
    db = SessionLocal()
    user = db.query(User).filter(User.email == current_user).first()
    post = db.query(Post).filter(Post.owner_id == user.id).all()
    # print("posts are: ", post)
    if post is None:
            raise HTTPException(status_code=404, detail="Post not found")
    
    db.close()
    return post 

@router.delete("/posts/{post_id}", response_model=PostSchema)
def delete_post(post_id: int,current_user = Depends(get_current_user)):
    db = SessionLocal()
    post = db.query(Post).filter(Post.id == post_id).first()
    user = db.query(User).filter(User.email == current_user).first()
    if post is None:
            raise HTTPException(status_code=404, detail="Post not found")
    if post.owner_id == user.id:
        db.delete(post)
        db.commit()
        db.close()
        return post
    else:
        raise HTTPException(status_code=404, detail="Post doesn't belong to the current user")

