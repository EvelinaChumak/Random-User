import pytest
from models.user import User
from config.info_for_api import InfoForProject


@pytest.fixture(scope="session")
def get_users():
    yield User.get_by_attr(results=InfoForProject.RESILTS)
