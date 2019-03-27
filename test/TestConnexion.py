import pytest

from app import app


class TestConnexion:
    """The base test providing auth and flask clients to other tests
    """
    cache: dict = {}
    CENTRAL_NODE_BASE_URL = os.environ.setdefault('CENTRAL_NODE_BASE_URL', 'http://localhost:8080/api/v1')

    @pytest.fixture(scope='session')
    def client(self):
        with app.app.test_client() as c:
            yield c
            app.registerThread.stop()
