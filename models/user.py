from utils.create_url import CreateUrl
import requests
import json


class User():

    def __init__(self, **kwargs):
        self.gender = kwargs.get('gender')
        self.name = kwargs.get('name')
        self.location = kwargs.get('location')
        self.email = kwargs.get('email')
        self.login = kwargs.get('login')
        self.dob = kwargs.get('dob')
        self.registered = kwargs.get('registered')
        self.phone = kwargs.get('phone')
        self.cell = kwargs.get('cell')
        self.id = kwargs.get('id')
        self.picture = kwargs.get('id')
        self.nat = kwargs.get('nat')
        
    def __str__(self):
        return json.dumps(self.__dict__, indent=4)

    @classmethod
    def get_by_attr(cls, **info):
        url = CreateUrl.get_url(info)
        cls.response = requests.get(url=url).json()
        results = cls.response['results']
        users = [cls(**result) for result in results]
        return users[0] if len(users) == 1 else users
