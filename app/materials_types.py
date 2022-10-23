from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import login_required

from app.app import db
from app.models import MaterialType, MaterialGroup, MaterialClass, MaterialMeasureUnit


bp = Blueprint('materials_types', __name__, url_prefix='/materials_types')


@bp.route("/")
@login_required
def index():
    types = MaterialType.query.all()

    return render_template("materials_types/index.html", types=types)
    
@bp.route("/create", methods=['GET', 'POST'])
@login_required
def create():
    groups = MaterialGroup.query.all()
    classes = MaterialClass.query.all()
    measure_units = MaterialMeasureUnit.query.all()

    if request.method == "POST":
        type = MaterialType()
        type.name = request.form.get("type_name")
        type.group_id = request.form.get("type_group_id")
        type.class_id = request.form.get("type_class_id")
        type.measure_unit_id = request.form.get("type_measure_unit_id")

        db.session.add(type)
        db.session.commit()

        return redirect(url_for("materials_types.index"))

    return render_template("materials_types/create.html", groups=groups, classes=classes, measure_units=measure_units) 

@bp.route("/edit/<int:type_id>", methods=['GET', 'POST'])
@login_required
def edit(type_id):
    type = MaterialType.query.get(type_id)
    groups = MaterialGroup.query.all()
    classes = MaterialClass.query.all()
    measure_units = MaterialMeasureUnit.query.all()

    if request.method == "POST":
        type.name = request.form.get("type_name")
        type.group_id = request.form.get("type_group_id")
        type.class_id = request.form.get("type_class_id")
        type.measure_unit_id = request.form.get("type_measure_unit_id")

        db.session.commit()

        return redirect(url_for("materials_types.index"))

    return render_template("materials_types/edit.html", type=type, groups=groups, classes=classes, measure_units=measure_units) 

@bp.route("/delete/<int:type_id>", methods=['POST'])
@login_required
def delete(type_id):
    type = MaterialType.query.get(type_id)

    db.session.delete(type)
    db.session.commit()

    return redirect(url_for("materials_types.index"))


@bp.route("/groups")
@login_required
def groups():
    groups = MaterialGroup.query.all()

    return render_template("materials_types/groups/groups.html", groups=groups)

@bp.route("/groups/create", methods=['GET', 'POST'])
@login_required
def create_group():
    if request.method == "POST":
        group = MaterialGroup()
        group.name = request.form.get("group_name")

        db.session.add(group)
        db.session.commit()

        return redirect(url_for("materials_types.groups"))

    return render_template("materials_types/groups/create_group.html")

@bp.route("/groups/edit/<int:group_id>", methods=['GET', 'POST'])
@login_required
def edit_group(group_id):
    group = MaterialGroup.query.get(group_id)

    if request.method == "POST":
        group.name = request.form.get("group_name")

        db.session.commit()

        return redirect(url_for("materials_types.groups"))

    return render_template("materials_types/groups/edit_group.html", group=group)

@bp.route("/groups/delete/<int:group_id>", methods=['POST'])
@login_required
def delete_group(group_id):
    group = MaterialGroup.query.get(group_id)

    db.session.delete(group)
    db.session.commit()

    return redirect(url_for("materials_types.groups"))


@bp.route("/classes")
@login_required
def classes():
    classes = MaterialClass.query.all()

    return render_template("materials_types/classes/classes.html", classes=classes)

@bp.route("/classes/create", methods=['GET', 'POST'])
@login_required
def create_class():
    if request.method == "POST":
        _class = MaterialClass()
        _class.name = request.form.get("class_name")

        db.session.add(_class)
        db.session.commit()

        return redirect(url_for("materials_types.classes"))

    return render_template("materials_types/classes/create_class.html")

@bp.route("/classes/edit/<int:class_id>", methods=['GET', 'POST'])
@login_required
def edit_class(class_id):
    _class = MaterialClass.query.get(class_id)

    if request.method == "POST":
        _class.name = request.form.get("class_name")

        db.session.commit()

        return redirect(url_for("materials_types.classes"))

    return render_template("materials_types/classes/edit_class.html", _class=_class)

@bp.route("/classes/delete/<int:class_id>", methods=['POST'])
@login_required
def delete_class(class_id):
    _class = MaterialGroup.query.get(class_id)

    db.session.delete(_class)
    db.session.commit()

    return redirect(url_for("materials_types.classes"))


@bp.route("/measure_units")
@login_required
def measure_units():
    measure_units = MaterialMeasureUnit.query.all()

    return render_template("materials_types/measure_units/measure_units.html", measure_units=measure_units)

@bp.route("/measure_units/create", methods=['GET', 'POST'])
@login_required
def create_measure_unit():
    if request.method == "POST":
        measure_unit = MaterialMeasureUnit()
        measure_unit.name = request.form.get("measure_unit_name")

        db.session.add(measure_unit)
        db.session.commit()

        return redirect(url_for("materials_types.measure_units"))

    return render_template("materials_types/measure_units/create_measure_unit.html")

@bp.route("/measure_units/edit/<int:measure_unit_id>", methods=['GET', 'POST'])
@login_required
def edit_measure_unit(measure_unit_id):
    measure_unit = MaterialMeasureUnit.query.get(measure_unit_id)

    if request.method == "POST":
        measure_unit.name = request.form.get("measure_unit_name")

        db.session.commit()

        return redirect(url_for("materials_types.measure_units"))

    return render_template("materials_types/measure_units/edit_measure_unit.html", measure_unit=measure_unit)

@bp.route("/measure_units/delete/<int:measure_unit_id>", methods=['POST'])
@login_required
def delete_measure_unit(measure_unit_id):
    measure_unit = MaterialMeasureUnit.query.get(measure_unit_id)

    db.session.delete(measure_unit)
    db.session.commit()

    return redirect(url_for("materials_types.measure_units")) 
