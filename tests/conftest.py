from red import create_app
from red.settings import get_config
import pytest


@pytest.fixture
def app():
    app = create_app(get_config('test'))
    app.testing = True
    return app
