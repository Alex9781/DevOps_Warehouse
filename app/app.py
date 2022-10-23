from flask import Flask, url_for, redirect
from flask_login import login_required
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_pyfile("config.py")


convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}


metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(app, metadata=metadata)
migrate = Migrate(app, db)


from app.auth import bp as auth_bp, init_login_manager
from app.orders import bp as orders_bp
from app.shippers import bp as shippers_bp
from app.documents import bp as documents_bp
from app.materials_types import bp as materials_types_bp


app.register_blueprint(auth_bp)
app.register_blueprint(orders_bp)
app.register_blueprint(shippers_bp)
app.register_blueprint(documents_bp)
app.register_blueprint(materials_types_bp)
init_login_manager(app)


@app.route("/")
@login_required
def index():
    return redirect(url_for("orders.index"))
