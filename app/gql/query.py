from graphene import ObjectType, List

from app.db.database import session_maker
from app.db.models import UserDetails
from app.gql.types.user_type import UserType


class Query(ObjectType):
    all_users = List(UserType)

    @staticmethod
    def resolve_all_users(root, info):
        with session_maker() as session:
            return session.query(UserDetails).all()