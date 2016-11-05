import red
import pytest

@pytest.fixture
def app():
    # FIXME: Rebuild application every time
    red.application.testing = True
    return red.application