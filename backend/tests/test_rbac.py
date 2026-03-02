import pytest
from backend.app import create_app
from backend.extensions import db
from backend.services.rbac_service import RBACService


@pytest.fixture
def app():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

    with app.app_context():
        db.drop_all()
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


def test_admin_can_delete(client):
    RBACService.create_permission("delete_user")
    RBACService.create_role("admin")
    RBACService.assign_permission_to_role("admin", "delete_user")
    RBACService.create_user("alice", "admin")

    response = client.post(
        "/delete-user",
        headers={"X-Username": "alice"}
    )

    assert response.status_code == 200


def test_viewer_cannot_delete(client):
    RBACService.create_permission("delete_user")
    RBACService.create_role("viewer")
    RBACService.create_user("bob", "viewer")

    response = client.post(
        "/delete-user",
        headers={"X-Username": "bob"}
    )

    assert response.status_code == 403