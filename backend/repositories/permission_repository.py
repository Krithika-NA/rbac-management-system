from backend.extensions import db
from backend.models.permission import Permission

class PermissionRepository:

    @staticmethod
    def create(name):
        permission = Permission(name=name)
        db.session.add(permission)
        db.session.commit()
        return permission

    @staticmethod
    def get_by_name(name):
        return Permission.query.filter_by(name=name).first()

    @staticmethod
    def get_all():
        return Permission.query.all()