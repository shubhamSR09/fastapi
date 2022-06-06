from email.policy import default
from fastapi import FastAPI,Query, Depends
from typing  import Optional,List
from pydantic import BaseModel
from sqlalchemy import Column,String,Integer,Boolean


from database import Base, engine, SessionLocal

class User(Base):
    __tablename__="users23"
    id=Column(Integer,primary_key=True, index=True)
    email=Column(String,unique=True,index=True)
    is_active=Column(Boolean,default=True)



Base.metadata.create_all(bind=engine)

app=FastAPI()

