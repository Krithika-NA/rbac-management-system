from backend.repositories.user_repository import UserRepository
from backend.repositories.role_repository import RoleRepository
from backend.repositories.permission_repository import PermissionRepository

class RBACService:

    @staticmethod
    def create_permission(name):
        existing = PermissionRepository.get_by_name(name)
        if existing:
            raise ValueError("Permission already exists")
        return PermissionRepository.create(name)

    @staticmethod
    def create_role(name):
        existing = RoleRepository.get_by_name(name)
        if existing:
            raise ValueError("Role already exists")
        return RoleRepository.create(name)

    @staticmethod
    def assign_permission_to_role(role_name, permission_name):
        role = RoleRepository.get_by_name(role_name)
        permission = PermissionRepository.get_by_name(permission_name)

        if not role:
            raise ValueError("Role not found")

        if not permission:
            raise ValueError("Permission not found")

        RoleRepository.add_permission(role, permission)

    @staticmethod
    def create_user(username, role_name):
        existing = UserRepository.get_by_username(username)
        if existing:
            raise ValueError("User already exists")

        role = RoleRepository.get_by_name(role_name)
        if not role:
            raise ValueError("Role not found")

        return UserRepository.create(username, role)

    @staticmethod
    def check_permission(username, permission_name):
        user = UserRepository.get_by_username(username)

        if not user:
            raise ValueError("User not found")

        return any(p.name == permission_name for p in user.role.permissions)