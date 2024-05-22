import pytest
from src.main import build_app


@pytest.fixture
def app():
    app = build_app()
    app.config['TESTING'] = True
    yield app


@pytest.fixture
def client(app):
    return app.test_client()