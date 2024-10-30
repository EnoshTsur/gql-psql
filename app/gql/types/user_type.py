from graphene import ObjectType, Int, String


class UserType(ObjectType):
    id = Int
    first_name = String()
    last_name = String()
    email = String()
    user_type = String()
    identifier = String()