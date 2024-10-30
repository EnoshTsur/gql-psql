# tablename, id, (card_number - string), ( cvv - integer ), (expiration - date), identifier -string
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.db.models import Base

class CreditCard(Base):
    __tablename__ = "credit_card"
    id = Column(Integer, primary_key=True, autoincrement=True)
    card_number = Column(String, nullable=False)
    cvv = Column(Integer, nullable=False)
    expiration = Column(Date, nullable=False)
    identifier = Column(String)
    user_id = Column(Integer, ForeignKey("user_details.id"))

    user = relationship("UserDetails", back_populates="credit_cards")