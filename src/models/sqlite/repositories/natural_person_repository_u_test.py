from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.sqlite.entities.natural_person import NaturalPersonTable
from .natural_person_repository import NaturalPersonRepository

class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(NaturalPersonTable)],
                    [
                        NaturalPersonTable(full_name="john smith1", age= 35, email="email", category="category", cellphone_number="cellphone_number", cpf="cpf", balance=1000, monthly_income=50),
                        NaturalPersonTable(full_name="john smith2", age= 35, email="email", category="category", cellphone_number="cellphone_number", cpf="cpf", balance=1000, monthly_income=50),
                    ]
                )
            ]
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


def test_insert_natural_person():
    mock_connection = MockConnection()
    repo = NaturalPersonRepository(mock_connection)

    repo.insert_natural_person("john smith", 35, "johnsmith@gmail.com", "D", "99999-9999", "999.999.999-99", 10000, 5000)

    assert mock_connection.session.add.called
    mock_connection.session.commit.assert_called_once()

def test_delete_natural_person():
    mock_connection = MockConnection()
    repo = NaturalPersonRepository(mock_connection)

    repo.delete_natural_person("personname")

    mock_connection.session.query.assert_called_once_with(NaturalPersonTable)
    mock_connection.session.filter.assert_called_once_with(NaturalPersonTable.full_name == "personname")
    mock_connection.session.delete.assert_called_once()

def test_list_natural_person():
    mock_connection = MockConnection()
    repo = NaturalPersonRepository(mock_connection)

    repo.list_natural_person("personname")

    mock_connection.session.query.assert_called_once_with(NaturalPersonTable)
    mock_connection.session.filter.assert_called_once_with(NaturalPersonTable.full_name == "personname")
    mock_connection.session.all.assert_not_called()

def test_list_all_natural_person():
    mock_connection = MockConnection()
    repo = NaturalPersonRepository(mock_connection)

    response = repo.list_all_natural_person()

    mock_connection.session.query.assert_called_once_with(NaturalPersonTable)
    mock_connection.session.all.assert_called()
    mock_connection.session.filter.assert_not_called()

    assert response[0].full_name == "john smith1"
    assert response[1].full_name == "john smith2"

def test_change_balance_natural_person():
    mock_connection = MockConnection()
    repo = NaturalPersonRepository(mock_connection)

    repo.change_balance_natural_person("personname", 1000)

    mock_connection.session.execute.assert_called()
    mock_connection.session.commit.assert_called_once()


    
