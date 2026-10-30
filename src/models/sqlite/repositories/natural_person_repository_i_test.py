import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.natural_person_repository import NaturalPersonRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Interation with the db test")
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

@pytest.mark.skip(reason="Interation with the db test")
def test_delete_natural_person():
    name = "john smithss"
    repo = NaturalPersonRepository(db_connection_handler)
    repo.delete_natural_person(name)

@pytest.mark.skip(reason="Interation with the db test")
def test_list_natural_person():
    name = "john smith"
    repo = NaturalPersonRepository(db_connection_handler)
    person_found = repo.list_natural_person(name)

    print()
    print(person_found)

@pytest.mark.skip(reason="Interation with the db test")
def test_list_all_natural_person():
    repo = NaturalPersonRepository(db_connection_handler)
    all_natural_people = repo.list_all_natural_person()

    print()
    print(all_natural_people)

@pytest.mark.skip(reason="Interation with the db test")
def test_change_balance_natural_person():
    name = "João da Silva"
    repo = NaturalPersonRepository(db_connection_handler)
    repo.change_balance_natural_person(name, 500000)