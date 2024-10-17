from sqlalchemy import Column, BigInteger, Integer, String, Float, Text, TIMESTAMP
from .database import Base

class Gedebie(Base):
    __tablename__ = "gedebie"

    message_id = Column(BigInteger, primary_key=True, index=True, name="Message ID")
    sender = Column(BigInteger, name="Sender")
    image_name = Column(String(255), name="image_name")
    class_id = Column(Integer, name="class_id")
    confidence = Column(Float, name="confidence")
    bbox = Column(Text, name="bbox")
    date = Column(TIMESTAMP(timezone=True), name="Date")
    message = Column(Text, name="Message")
