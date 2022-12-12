from flask import Flask, url_for, redirect
from flask_login import login_required
from app.models import db

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)

    db.init_app(app)

    from app.auth import bp as auth_bp, init_login_manager
    from app.orders import bp as orders_bp
    from app.shippers import bp as shippers_bp
    from app.documents import bp as documents_bp
    from app.materials_types import bp as materials_types_bp
    from app.calculations import bp as calculations_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(orders_bp)
    app.register_blueprint(shippers_bp)
    app.register_blueprint(documents_bp)
    app.register_blueprint(materials_types_bp)
    app.register_blueprint(calculations_bp)
    init_login_manager(app)

    @app.route("/")
    @login_required
    def index():
        return redirect(url_for("orders.index"))

    return app

app = create_app("config.py")
