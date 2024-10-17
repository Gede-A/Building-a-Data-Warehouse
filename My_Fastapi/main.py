from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from My_Fastapi import models, schemas, crud
from .database import SessionLocal, engine, get_db

# Initialize the FastAPI app
app = FastAPI()

# Create database tables
models.Base.metadata.create_all(bind=engine)

@app.post("/messages/", response_model=schemas.Gedebie)
def create_message(message: schemas.GedebieCreate, db: Session = Depends(get_db)):
    return crud.create_message(db=db, message=message)

@app.get("/messages/{message_id}", response_model=schemas.Gedebie)
def read_message(message_id: int, db: Session = Depends(get_db)):
    db_message = crud.get_message(db, message_id=message_id)
    if db_message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    return db_message

@app.get("/messages/", response_model=list[schemas.Gedebie])
def read_messages(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    messages = crud.get_messages(db, skip=skip, limit=limit)
    return messages
