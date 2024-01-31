from fastapi import FastAPI,HTTPException,Depends,status
import models
from typing import Annotated
from pydantic import BaseModel
from database import engine,SessionLocal
from sqlalchemy.orm import session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class PostBase(BaseModel):
    title = str
    content = str
    user_id = int

class UserBase(BaseModel):
    username: str