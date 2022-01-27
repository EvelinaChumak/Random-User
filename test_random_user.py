from config.info_for_api import InfoForProject
import pytest
import re
import datetime


class TestRandomUser():

    def test_user_nat_phohe(self, get_users):
        users = get_users

        assert len(users) == InfoForProject.RESILTS, 'Получено: {}, ожидалось: {}'.format(
            len(users), InfoForProject.RESILTS)

        assert all(user.nat in InfoForProject.NAT for user in users), \
            'Национальности {} нет в списке {}'.format(
                [user.nat for user in users], InfoForProject.NAT)

        m = re.fullmatch(InfoForProject.NUMBER_FORMAT, users[0].phone)
        assert all(True if re.fullmatch(InfoForProject.NUMBER_FORMAT_R,
                   user.phone) else False for user in users), \
            'Номера {} не соотвествуют формату {}'.format(
                [user.phone for user in users], InfoForProject.NUMBER_FORMAT)


    def test_age_picture(self, get_users):
        users = get_users
        users_date = [datetime.date(
            *(int(_) for _ in user.dob['date'].split('T')[0].split('-'))) for user in users]
        users_age = [user.dob['age'] for user in users]
        current_date = datetime.date.today()
        our_users_age = [int((current_date-user_date).days/365)
                         for user_date in users_date]
        assert users_age == our_users_age, 'Возрост с сайта: {}, возрост на текущий момент: {}'.format(
            users_age, our_users_age)
