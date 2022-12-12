import pytest
from app.app import create_app
from app.calculations import calculation_one

from app.models import Order, Shipper

@pytest.fixture()
def app():
    from dotenv import load_dotenv
    load_dotenv()
    app = create_app("config.py")
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()

def test_calcaulation_one_correct_2():  # Проверка,что два уникальных поставщика
    test = [Order(
        id = 1,
        supply_date = '2022-13-12',
        material_count = 10,
        balance_account = 1234,
        shipper_id = 1,
        document_id = 4,
        material_type_id = 2,
    ), Order(
        id = 2,
        supply_date = '2022-13-12',
        material_count = 10,
        balance_account = 1234,
        shipper_id = 2,
        document_id = 4,
        material_type_id = 2,
    )]
    assert calculation_one(test) == 2

def test_calcaulation_two_correct_1():   # Проверка,что один уникальный поставщик
    test = [Order(
        id = 1,
        supply_date = '2022-13-12',
        material_count = 10,
        balance_account = 1234,
        shipper_id = 1,
        document_id = 4,
        material_type_id = 2,
    ), Order(
        id = 2,
        supply_date = '2022-13-12',
        material_count = 10,
        balance_account = 1234,
        shipper_id = 1,
        document_id = 4,
        material_type_id = 2,
    )]
    assert calculation_one(test) == 1