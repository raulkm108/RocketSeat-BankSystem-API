from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from .natural_person_repository import NaturalPersonRepository

class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock()

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