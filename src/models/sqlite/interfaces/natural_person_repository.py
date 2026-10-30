from typing import List
from abc import ABC, abstractmethod
from src.models.sqlite.entities.natural_person import NaturalPersonTable #pylint: disable=unused-import


class NaturalPersonInterface(ABC):

    @abstractmethod
    def insert_natural_person(self, full_name:str, age:int, email:str, category: str, cellphone_number:str, cpf:str, balance:float, monthly_income:float) ->  None:
        pass

    @abstractmethod
    def delete_natural_person(self, full_name:str) ->  None:
        pass

    @abstractmethod
    def list_natural_person(self, full_name:str) ->  NaturalPersonTable:
        pass

    @abstractmethod
    def list_all_natural_person(self) ->  List:
        pass