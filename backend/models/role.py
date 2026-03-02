from backend.extensions import db

role_permissions = db.Table(
    "role_permissions",
    db.Column("role_id", db.Integer, db.ForeignKey("roles.id")),
    db.Column("permission_id", db.Integer, db.ForeignKey("permissions.id"))
)

class Role(db.Model):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    permissions = db.relationship(
        "Permission",
        secondary=role_permissions,
        backref="roles"
    )

    def __repr__(self):
        return f"<Role {self.name}>"