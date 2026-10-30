from typing import List
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import update
from src.models.sqlite.entities.natural_person import NaturalPersonTable
from src.models.sqlite.interfaces.natural_person_repository import NaturalPersonInterface

class NaturalPersonRepository(NaturalPersonInterface):
    def __init__(self, db_connection):
        self.__db_connection = db_connection

    def insert_natural_person(self, full_name:str, age:int, email:str, category: str, cellphone_number:str, cpf:str, balance:float, monthly_income:float) ->  None:
        with self.__db_connection as database:
            try:
                natural_person_data = NaturalPersonTable(full_name=full_name, age=age, email=email, category=category, cellphone_number=cellphone_number, cpf=cpf, balance=balance, monthly_income=monthly_income)
                database.session.add(natural_person_data)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def delete_natural_person(self, full_name:str) -> None:
        with self.__db_connection as database:
            try:
                (
                    database.session.query(NaturalPersonTable).filter(NaturalPersonTable.full_name == full_name).delete()
                )
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception


    def list_natural_person(self, full_name:str) -> NaturalPersonTable:
        with self.__db_connection as database:
            try:
                natural_person = (
                    database.session.query(NaturalPersonTable).filter(NaturalPersonTable.full_name == full_name).first()
                )
                return natural_person
            except NoResultFound:
                return None

    def list_all_natural_person(self) -> List:
        with self.__db_connection as database:
            try:
                all_natural_people = database.session.query(NaturalPersonTable).all()
                return all_natural_people
            except NoResultFound:
                return []

    def change_balance_natural_person(self,full_name:str, new_balance:float) -> int:
        with self.__db_connection as database:
            database.session.execute(update(NaturalPersonTable).where(NaturalPersonTable.full_name == full_name).values(balance=new_balance))
            database.session.commit()