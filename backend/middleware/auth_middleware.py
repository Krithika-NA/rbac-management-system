from functools import wraps
from flask import request, jsonify
from backend.services.rbac_service import RBACService

def require_permission(permission_name):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            username = request.headers.get("X-Username")

            if not username:
                return jsonify({
                    "error": "Unauthorized",
                    "message": "Username header missing"
                }), 401

            try:
                allowed = RBACService.check_permission(username, permission_name)
            except ValueError as e:
                return jsonify({"error": str(e)}), 404

            if not allowed:
                return jsonify({
                    "error": "Forbidden",
                    "message": f"Missing permission: {permission_name}"
                }), 403

            return func(*args, **kwargs)

        return wrapper
    return decorator