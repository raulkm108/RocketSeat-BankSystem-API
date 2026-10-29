from src.models.sqlite.entities.natural_person import NaturalPersonTable

class NaturalPersonRepository():
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