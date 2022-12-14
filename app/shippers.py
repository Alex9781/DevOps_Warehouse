from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required
from sqlalchemy import exc

from app.models import db, Shipper, Bank


bp = Blueprint('shippers', __name__, url_prefix='/shippers')


@bp.route("/")
@login_required
def index():
    shippers = Shipper.query.all()

    return render_template("shippers/index.html", shippers=shippers)

@bp.route("/create", methods=['GET', 'POST'])
@login_required
def create():
    if request.method == "POST":
        shipper = Shipper()
        shipper.name = request.form.get("shipper_name")
        shipper.address = request.form.get("shipper_address")
        shipper.tax_number = request.form.get("shipper_tax_number")
        shipper.bill_number = request.form.get("shipper_bill_number")
        shipper.bank_id = request.form.get("shipper_bank_id")

        db.session.add(shipper)
        db.session.commit()

        return redirect(url_for("shippers.index"))

    banks = Bank.query.all()
    return render_template("shippers/create.html", banks=banks)

@bp.route("/edit/<int:shipper_id>", methods=['GET', 'POST'])
@login_required
def edit(shipper_id):
    banks = Bank.query.all()
    shipper = Shipper.query.get(shipper_id)

    if request.method == "POST":
        shipper.name = request.form.get("shipper_name")
        shipper.address = request.form.get("shipper_address")
        shipper.tax_number = request.form.get("shipper_tax_number")
        shipper.bill_number = request.form.get("shipper_bill_number")
        shipper.bank_id = request.form.get("shipper_bank_id")

        db.session.commit()

        return redirect(url_for("shippers.index"))

    return render_template("shippers/edit.html", shipper=shipper, banks=banks)

@bp.route("/delete/<int:shipper_id>", methods=["POST"])
@login_required
def delete(shipper_id):
    try:
        shipper = Shipper.query.get(shipper_id)

        db.session.delete(shipper)
        db.session.commit()

    except exc.SQLAlchemyError:
        flash("Невозможно удалить заказчика, если от него зависят заказы. Сначала удалите все заказы, зависящие от этого заказчика.", "danger")

    return redirect(url_for("shippers.index"))


@bp.route("/banks")
@login_required
def banks():
    banks = Bank.query.all()

    return render_template("shippers/banks/banks.html", banks=banks)

@bp.route("/banks/create", methods=['GET', 'POST'])
@login_required
def create_bank():
    if request.method == "POST":
        bank = Bank()
        bank.name = request.form.get("bank_name")
        bank.address = request.form.get("bank_address")

        db.session.add(bank)
        db.session.commit()

        return redirect(url_for("shippers.banks"))

    return render_template("shippers/banks/create_bank.html")

@bp.route("/banks/edit/<int:bank_id>", methods=['GET', 'POST'])
@login_required
def edit_bank(bank_id):
    bank =  Bank.query.get(bank_id)

    if request.method == "POST":
        bank.name = request.form.get("bank_name")
        bank.address = request.form.get("bank_address")

        db.session.commit()

        return redirect(url_for("shippers.banks"))

    return render_template("shippers/banks/edit_bank.html", bank=bank)

@bp.route("/banks/delete/<int:bank_id>", methods=["POST"])
@login_required
def delete_bank(bank_id):
    try:
        bank = Bank.query.get(bank_id)

        db.session.delete(bank)
        db.session.commit()
    except exc.SQLAlchemyError:
        flash("Невозможно удалить банк, если от него зависят поставщики. Сначала удалите всех поставщиков, зависящих от этого банка.", "danger")

    return redirect(url_for("shippers.banks"))
    