from app.models.user import User
from app.schemas.user_schema import UserSchema
from app.extensions import db

user_schema = UserSchema()
users_schema = UserSchema(many=True)

def users():
    users = User.query.all()
    return users_schema.dump(users)

def user(data):
    user = user_schema.load(data)
    db.session.add(user)
    db.session.commit()
    return user_schema.dump(user), 201