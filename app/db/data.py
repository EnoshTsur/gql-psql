from returns.result import Failure
from sqlalchemy.testing.suite.test_reflection import users

from app.db.database import engine
from app.db.models import UserDetails, Base
from app.repository.user_repository import create_many_users

users_data = [
        UserDetails(
            first_name="enosh",
            last_name="tsur",
            email="enosh@walla.com",
            identifier="302751451",
            user_type="regular"
        ),
        UserDetails(
            first_name="omer",
            last_name="munk",
            email="em@walla.com",
            identifier="302751441",
            user_type="regular"
        ),
        UserDetails(
            first_name="alef",
            last_name="lewit",
            email="al@walla.com",
            identifier="12328893",
            user_type="regular"
        ),
    ]

def init_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    res = create_many_users(users_data)
    if isinstance(res, Failure):
        raise Exception(res.failure())