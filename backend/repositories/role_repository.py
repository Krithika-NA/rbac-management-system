from backend.extensions import db
from backend.models.role import Role
from backend.models.permission import Permission

class RoleRepository:

    @staticmethod
    def create(name):
        role = Role(name=name)
        db.session.add(role)
        db.session.commit()
        return role

    @staticmethod
    def get_by_name(name):
        return Role.query.filter_by(name=name).first()

    @staticmethod
    def add_permission(role, permission):
        role.permissions.append(permission)
        db.session.commit()