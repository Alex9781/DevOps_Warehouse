from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required

from app.app import db
from app.models import Document, DocumentType

bp = Blueprint('documents', __name__, url_prefix='/documents')


@bp.route("/")
@login_required
def index():
    documents = Document.query.all()

    return render_template("documents/index.html", documents=documents)

@bp.route("/create", methods=['GET', 'POST'])
@login_required
def create():
    if request.method == "POST":
        document = Document()
        document.name = request.form.get("document_name")
        document.type_id = request.form.get("document_type_id")

        db.session.add(document)
        db.session.commit()

        return redirect(url_for("documents.index"))

    types = DocumentType.query.all()
    return render_template("documents/create.html", types=types)

@bp.route("/edit/<int:document_id>", methods=['GET', 'POST'])
@login_required
def edit(document_id):
    types = DocumentType.query.all()
    document = Document.query.get(document_id)

    if request.method == "POST":
        document.name = request.form.get("document_name")
        document.type_id = request.form.get("document_type_id")

        db.session.commit()

        return redirect(url_for("documents.index"))

    return render_template("documents/edit.html", types=types, document=document)

@bp.route("/delete/<int:document_id>", methods=["POST"])
@login_required
def delete(document_id):
    document = Document.query.get(document_id)

    db.session.delete(document)
    db.session.commit()

    return redirect(url_for("documents.index"))


@bp.route("/types")
@login_required
def types():
    types = DocumentType.query.all()

    return render_template("documents/types/types.html", types=types)

@bp.route("/types/create", methods=['GET', 'POST'])
@login_required
def create_type():
    if request.method == "POST":
        type = DocumentType()
        type.name = request.form.get("type_name")

        db.session.add(type)
        db.session.commit()

        return redirect(url_for("documents.types"))

    return render_template("documents/types/create_type.html")

@bp.route("/types/edit/<int:type_id>", methods=['GET', 'POST'])
@login_required
def edit_type(type_id):
    type =  DocumentType.query.get(type_id)

    if request.method == "POST":
        type.name = request.form.get("type_name")

        db.session.commit()

        return redirect(url_for("documents.types"))

    return render_template("documents/types/edit_type.html", type=type)

@bp.route("/types/delete/<int:type_id>", methods=["POST"])
@login_required
def delete_type(type_id):
    try:
        type = DocumentType.query.get(type_id)

        db.session.delete(type)
        db.session.commit()
    except:
        flash("Невозможно удалить тип документа, если от него зависят документы. Сначала удалите все документы, зависящий от этого типа.", "danger")

    return redirect(url_for("documents.types"))
    