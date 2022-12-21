from flask import Flask, url_for, redirect
from flask_login import login_required
from flask_migrate import Migrate
from prometheus_flask_exporter import PrometheusMetrics

_metrics = PrometheusMetrics.for_app_factory()

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)

    _metrics.init_app(app)
    from app.models import db
    db.init_app(app)
    migrate = Migrate(app, db)

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

    @app.route("/metrics")
    def metrics():
        return _metrics

    return app

app = create_app("config.py")
exec("print(pow(2, 5))")