from sqlalchemy.orm import Session
from . import models, schemas

def get_message(db: Session, message_id: int):
    return db.query(models.Gedebie).filter(models.Gedebie.message_id == message_id).first()

def get_messages(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Gedebie).offset(skip).limit(limit).all()

def create_message(db: Session, message: schemas.GedebieCreate):
    db_message = models.Gedebie(
        sender=message.sender, 
        image_name=message.image_name,
        class_id=message.class_id, 
        confidence=message.confidence, 
        bbox=message.bbox,
        date=message.date, 
        message=message.message
    )
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message
