from returns.result import Result, Success, Failure
from typing import List
from app.db.database import session_maker
from app.db.models import UserDetails


def create_user(user: UserDetails) -> Result[UserDetails, str]:
    with session_maker() as session:
        try:
            session.add(user)
            session.commit()
            session.refresh(user)
            return Success(user)
        except Exception as e:
            session.rollback()
            return Failure(str(e))


def create_many_users(users: List[UserDetails]) -> Result[bool, str]:
    with session_maker() as session:
        try:
            session.add_all(users)
            session.commit()
            return Success(True)
        except Exception as e:
            session.rollback()
            return Failure(str(e))