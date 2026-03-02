from flask import Blueprint, request, jsonify
from backend.services.rbac_service import RBACService
from backend.middleware.auth_middleware import require_permission

rbac_bp = Blueprint("rbac", __name__)

@rbac_bp.route("/permission", methods=["POST"])
def create_permission():
    data = request.get_json()
    name = data.get("name")

    try:
        permission = RBACService.create_permission(name)
        return jsonify({"message": f"Permission '{permission.name}' created"})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@rbac_bp.route("/role", methods=["POST"])
def create_role():
    data = request.get_json()
    name = data.get("name")

    try:
        role = RBACService.create_role(name)
        return jsonify({"message": f"Role '{role.name}' created"})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@rbac_bp.route("/assign-permission", methods=["POST"])
def assign_permission():
    data = request.get_json()
    role_name = data.get("role_name")
    permission_name = data.get("permission_name")

    try:
        RBACService.assign_permission_to_role(role_name, permission_name)
        return jsonify({"message": "Permission assigned to role"})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@rbac_bp.route("/user", methods=["POST"])
def create_user():
    data = request.get_json()
    username = data.get("username")
    role_name = data.get("role_name")

    try:
        user = RBACService.create_user(username, role_name)
        return jsonify({"message": f"User '{user.username}' created"})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@rbac_bp.route("/delete-user", methods=["POST"])
@require_permission("delete_user")
def delete_user():
    return jsonify({"message": "User deleted successfully (simulated)"})