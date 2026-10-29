from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.natural_person_repository import NaturalPersonRepository

db_connection_handler.connect_to_db()

def test_insert_natural_person():

    full_name = "john smith"
    age = 35
    email = "johnsmith@gmail.com"
    category = "D"
    cellphone_number = "99999-9999"
    cpf = "999.999.999-99"
    balance = 5000
    monthly_income = 3000
    repo = NaturalPersonRepository(db_connection_handler)
    repo.insert_natural_person(full_name, age, email, category, cellphone_number, cpf, balance, monthly_income)
