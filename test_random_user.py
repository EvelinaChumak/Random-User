from models.user import User
from config.info_for_api import InfoForProject
import pytest
import re


class TestRandomUser():

    def test_user_nat_phohe(self, get_users):
        users = get_users

        assert len(users) == InfoForProject.RESILTS, 'Получено: {}, ожидалось: {}'.format(
            len(users), InfoForProject.RESILTS)

        assert all(user.nat in InfoForProject.NAT for user in users), \
            'Национальности {} нет в списке {}'.format(
                [user.nat for user in users], InfoForProject.NAT)

        print([user.phone for user in users])
        m = re.fullmatch(InfoForProject.NUMBER_FORMAT, users[0].phone)
        print()
        assert all(True if re.fullmatch(InfoForProject.NUMBER_FORMAT_R,
                   user.phone) else False for user in users), \
            'Номера {} не соотвествуют формату {}'.format(
                [user.phone for user in users], InfoForProject.NUMBER_FORMAT)
