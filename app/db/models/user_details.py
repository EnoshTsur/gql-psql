# tablename, id, firstname, lastname, email
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.models import Base

# regular, premium

class UserDetails(Base):
    __tablename__ = "user_details"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    user_type =Column(String, nullable=False)
    identifier = Column(String, nullable=False)

    credit_cards = relationship(
        "CreditCard",
        back_populates="user",
        cascade="all, delete-orphan"
    )
    address = relationship(
        "Address",
        uselist=False,
        back_populates="user",
        cascade="all, delete-orphan"
    )