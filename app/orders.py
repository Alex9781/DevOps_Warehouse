from flask import Blueprint, render_template, request, url_for, redirect, flash
from flask_login import login_required
from sqlalchemy import exc

from app.models import db, Order, Shipper, Document, MaterialType


bp = Blueprint('orders', __name__, url_prefix='/orders')


@bp.route("/")
@login_required
def index():
    orders = Order.query.all()

    return render_template("orders/index.html", orders=orders)
    
@bp.route("/create", methods=["GET", "POST"])
@login_required
def create():
    shippers = Shipper.query.all()
    documents = Document.query.all()
    materials_types = MaterialType.query.all()

    if request.method == "POST":
        order = Order()
        order.id = request.form.get("order_id")
        order.supply_date = request.form.get("order_date")
        order.material_count = request.form.get("material_count")
        order.balance_account = request.form.get("balance_account")
        order.shipper_id = request.form.get("shipper_id")
        order.document_id = request.form.get("document_id")
        order.material_type_id = request.form.get("material_type_id")

        db.session.add(order)
        db.session.commit()

        return redirect(url_for("orders.index"))

    return render_template("orders/create.html", shippers=shippers, documents=documents, materials_types=materials_types)

@bp.route("/edit/<int:order_id>", methods=["GET", "POST"])
@login_required
def edit(order_id):
    order = Order.query.get(order_id)
    shippers = Shipper.query.all()
    documents = Document.query.all()
    materials_types = MaterialType.query.all()

    if request.method == "POST":
        order.id = request.form.get("order_id")
        order.supply_date = request.form.get("order_date")
        order.material_count = request.form.get("material_count")
        order.balance_account = request.form.get("balance_account")
        order.shipper_id = request.form.get("shipper_id")
        order.document_id = request.form.get("document_id")
        order.material_type_id = request.form.get("material_type_id")

        db.session.commit()

        return redirect(url_for("orders.index"))

    return render_template("orders/edit.html", order=order, shippers=shippers, documents=documents, materials_types=materials_types)

@bp.route("/delete/<int:order_id>", methods=["POST"])
@login_required
def delete(order_id):
    try:
        order = Order.query.get(order_id)

        db.session.delete(order)
        db.session.commit()
  
    except exc.SQLAlchemyError:
        flash('Нельзя удалить: есть зависимости', 'danger')

    return redirect(url_for("orders.index")) 