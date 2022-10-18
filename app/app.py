from random import randint
from flask import Flask, render_template, url_for, redirect
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

from models import *
from auth import bp as auth_bp, init_login_manager

app.register_blueprint(auth_bp)
init_login_manager(app)

@app.route("/")
def index():
    orders = Order.query
    return render_template("index.html", orders=orders)

@app.route("/edit/<int:order_id>", methods=['GET', 'POST'])
def edit(order_id):
    order = Order.query.get(order_id)
    #order.material_count = randint(1, 100)
    #order.balance_account = randint(1, 100)


    db.session.add(order)
    db.session.commit()

    return redirect(url_for("index"))

@app.route("/delete/<int:order_id>", methods=['POST'])
def delete(order_id):
    order = Order.query.get(order_id)

    db.session.delete(order)
    db.session.commit()

    return redirect(url_for("index"))

@app.route("/create", methods=['GET', 'POST'])
def create():
    order = Order()
    #order.material_count = randint(1, 100)
    #order.balance_account = randint(1, 100)
    order.shipper_id = 1
    order.document_id = 1
    order.material_type_id = 1

    db.session.add(order)
    db.session.commit()

    return redirect(url_for("index"))
