import pytest
from webtest import TestApp

from milkjug.api import Api

@pytest.fixture()
def app():
    app = Api()
    return app

@pytest.fixture()
def client(app):
    return TestApp(app)
