from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import engine, Base, get_db
import models
from pydantic import BaseModel
from typing import List, Optional

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Camp Management API - Sprint 1")

# Allow Frontend to communicate with Backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Pydantic Schemas ---
class UserCreate(BaseModel):
    name: str
    role: str

class GroupCreate(BaseModel):
    name: str

class CamperCreate(BaseModel):
    name: str
    parent_id: int
    group_id: Optional[int] = None

# --- API Endpoints ---
@app.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(name=user.name, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/")
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

@app.post("/groups/")
def create_group(group: GroupCreate, db: Session = Depends(get_db)):
    db_group = models.Group(name=group.name)
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group

@app.post("/campers/")
def create_camper(camper: CamperCreate, db: Session = Depends(get_db)):
    db_camper = models.Camper(name=camper.name, parent_id=camper.parent_id, group_id=camper.group_id)
    db.add(db_camper)
    db.commit()
    db.refresh(db_camper)
    return db_camper

@app.get("/campers/")
def get_campers(db: Session = Depends(get_db)):
    return db.query(models.Camper).all()