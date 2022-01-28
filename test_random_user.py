from config import InfoForProject
import pytest
import re
import datetime


class TestRandomUser():

    def test_user_nat_phohe(self, get_users_create_json):
        verification_errors = []

        users = get_users_create_json

        assert len(users) == InfoForProject.RESILTS, 'Получено: {}, ожидалось: {}'.format(
            len(users), InfoForProject.RESILTS)

        assert all(user.nat in InfoForProject.NAT for user in users), \
            'Национальности {} нет в списке {}'.format(
                [user.nat for user in users], InfoForProject.NAT)

        m = re.fullmatch(InfoForProject.NUMBER_FORMAT, users[0].phone)

        try:
            assert all(True if re.fullmatch(InfoForProject.NUMBER_FORMAT_R,
                                            user.phone) else False for user in users)
        except AssertionError:
            verification_errors.append('Номера {} не соотвествуют формату {}'.format(
                [user.phone for user in users], InfoForProject.NUMBER_FORMAT))

        assert len(verification_errors) == 0, ', '.join(verification_errors)

    def test_age_picture_email(self, get_users_create_json):
        users = get_users_create_json
        verification_errors = []
        
        users_date = [datetime.date(
            *(int(_) for _ in user.dob['date'].split('T')[0].split('-'))) for user in users]
        users_age = [user.dob['age'] for user in users]
        current_date = datetime.date.today()
        our_users_age = [int((current_date-user_date).days/365)
                         for user_date in users_date]

        try:
            assert users_age == our_users_age
        except AssertionError:
            verification_errors.append('Возрост с сайта: {}, возрост на текущий момент: {}'.format(
                users_age, our_users_age))

        pictures_value = [' ' if user.picture['value']
                          is None else user.picture['value'][0] for user in users]

        try:
            assert len(set(pictures_value)) == 1
        except AssertionError:
            verification_errors.append('Изображения начинаются с символов {}'.format(
                pictures_value))

        email = [user.email for user in users]

        try:
            assert len(set(email)) == len(users)
        except AssertionError:
            verification_errors.append('Email не уникальны {}'.format(email))

        assert len(verification_errors) == 0, ', '.join(verification_errors)
