import pytest
import json
from models import User
from config import InfoForProject


@pytest.fixture(scope="session")
def get_users_create_json():
    users = User.get_by_attr(results=InfoForProject.RESILTS)
    yield users

    res_json = {}
    for user in users:
        res_json[str((user.name['last'], user.email))
                 ] = user.phone.replace('-', '')

    with open('result.json', 'w') as outfile:
        json.dump(res_json, outfile, indent=4)
