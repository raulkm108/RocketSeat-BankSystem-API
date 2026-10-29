from unittest.mock import Mock
from sqlalchemy.engine import Engine
from .connection import DBConnectionHandler

def test_connect_to_db():

    db_connection_handler = DBConnectionHandler() #creating the instance inside the test instead of taking the created object makes the test more independent

    assert db_connection_handler.get_engine() is None

    db_connection_handler.connect_to_db()
    db_engine = db_connection_handler.get_engine()

    assert db_engine is not None
    assert isinstance(db_engine, Engine)

def test_session_is_closed(): #a test to check if the session actually closes

    db_connection_handler = DBConnectionHandler()
    db_connection_handler.connect_to_db()

    with db_connection_handler as handler:
        handler.session.close = Mock()

    handler.session.close.assert_called_once()