from flask import Blueprint, render_template, request
from flask_login import login_required


from app.app import db
from app.models import MaterialType, Order, Shipper, Bank


bp = Blueprint('calculations', __name__, url_prefix='/calculations')

def calculation_one(orders):
    res = []
    for order in orders:
            if order.shipper_id not in res:
                res.append(order.shipper_id)
    
    return len(res)

@bp.route("/", methods=['GET', 'POST'])
@login_required
def index():
    materials = MaterialType.query.all()
    result = None

    if request.method == "POST":
        material = request.form.get("material")
        orders = Order.query.filter(Order.material_type_id == material).distinct()
        result = calculation_one(orders)


    return render_template("calculations/index.html", materials=materials, result=result)

@bp.route("/second", methods=['GET', 'POST'])
@login_required
def second():
    materials = MaterialType.query.all()
    result = None

    if request.method == "POST":
        material = request.form.get("material")
        orders = Order.query.filter(Order.material_type_id == material).distinct()
        result = []
        for order in orders:
            shipper = Shipper.query.filter(Shipper.id == order.shipper_id).first()
            if shipper not in result:
                result.append(shipper)

    return render_template("calculations/second.html", materials=materials, shippers=result)

@bp.route("/third", methods=['GET', 'POST'])
@login_required
def third():
    banks = Bank.query.all()
    result = None

    if request.method == "POST":
        bank = request.form.get("bank")
        shipper = Shipper.query.filter(Shipper.bank_id == bank).count()
        result = shipper


    return render_template("calculations/third.html", banks=banks, result=result)