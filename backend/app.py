from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from backend.config import Config
from backend.extensions import db, migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    import backend.models.user
    import backend.models.role
    import backend.models.permission
    
    from backend.routes.rbac_routes import rbac_bp
    app.register_blueprint(rbac_bp)
    
    CORS(app)

    @app.route("/")
    def home():
        return {"message": "RBAC System Running"}

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)