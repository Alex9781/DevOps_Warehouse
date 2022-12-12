from sqlalchemy import sql
from flask_login import UserMixin
from werkzeug.security import check_password_hash
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)
db = SQLAlchemy()
migrate = Migrate(db)


class DBUser(db.Model, UserMixin):
    __tablename__ = "db_user"

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(256), nullable=False)

    def check_password(self, password: str):
        return check_password_hash(self.password_hash, password)

class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)

    supply_date = db.Column(db.DateTime, nullable=False, server_default=sql.func.now())
    material_count = db.Column(db.Integer, nullable=False)
    balance_account = db.Column(db.Integer, nullable=False)

    shipper_id = db.Column(db.Integer, db.ForeignKey("shippers.id"), nullable=False)
    document_id = db.Column(db.Integer, db.ForeignKey("documents.id"), nullable=False)
    material_type_id = db.Column(db.Integer, db.ForeignKey("materials_types.id"), nullable=False)

    shipper = db.relationship("Shipper")
    document = db.relationship("Document")
    material_type = db.relationship("MaterialType")

class Shipper(db.Model):
    __tablename__ = "shippers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    address = db.Column(db.Text, nullable=False)

    tax_number = db.Column(db.Integer, nullable=False, unique=True)
    bill_number = db.Column(db.Integer, nullable=False, unique=True)

    bank_id = db.Column(db.Integer, db.ForeignKey("banks.id"), nullable=False)

    bank = db.relationship("Bank")

class Bank(db.Model):
    __tablename__ = "banks"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

    address = db.Column(db.Text, nullable=False)

class Document(db.Model):
    __tablename__ = "documents"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    type_id = db.Column(db.Integer, db.ForeignKey("documents_types.id"), nullable=False)

    type = db.relationship("DocumentType")

class DocumentType(db.Model):
    __tablename__ = "documents_types"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

class MaterialType(db.Model):
    __tablename__ = "materials_types"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

    group_id = db.Column(db.Integer, db.ForeignKey("materials_groups.id"), nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey("materials_classes.id"), nullable=False)
    measure_unit_id = db.Column(db.Integer, db.ForeignKey("materials_measure_units.id"), nullable=False)

    group = db.relationship("MaterialGroup")
    _class = db.relationship("MaterialClass")
    unit = db.relationship("MaterialMeasureUnit")

class MaterialGroup(db.Model):
    __tablename__ = "materials_groups"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

class MaterialClass(db.Model):
    __tablename__ = "materials_classes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

class MaterialMeasureUnit(db.Model):
    __tablename__ = "materials_measure_units"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    