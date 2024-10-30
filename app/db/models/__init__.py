from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .user_details import UserDetails
from .credit_card import CreditCard
from .address import Address