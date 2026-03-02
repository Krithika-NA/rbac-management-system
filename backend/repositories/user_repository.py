from backend.extensions import db
from backend.models.user import User

class UserRepository:

    @staticmethod
    def create(username, role):
        user = User(username=username, role=role)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def get_by_username(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def get_all():
        return User.query.all()