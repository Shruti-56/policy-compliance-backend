from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .database import Base, engine, SessionLocal
from . import crud, schemas

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Policy & Compliance Management API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/policies", response_model=schemas.PolicyResponse)
def create_policy(policy: schemas.PolicyCreate, db: Session = Depends(get_db)):
    return crud.create_policy(db, policy)

@app.post("/policies/{policy_id}/versions")
def add_version(policy_id: int, version: schemas.PolicyVersionCreate, db: Session = Depends(get_db)):
    return crud.add_policy_version(db, policy_id, version)

@app.post("/policies/{policy_id}/acknowledge")
def acknowledge(policy_id: int, ack: schemas.AcknowledgementCreate, db: Session = Depends(get_db)):
    return crud.acknowledge_policy(db, policy_id, ack)
