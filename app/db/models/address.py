# state, city, street , street_number
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.models import Base

class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True, autoincrement=True)
    state = Column(String, nullable=False)
    city = Column(String, nullable=False)
    street = Column(String, nullable=False)
    street_number = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey("user_details.id"))

    user = relationship("UserDetails", back_populates="address")