from models.user import User
from config.info_for_api import InfoForProject

class TestRandomUser():
    
    def test_user_info(self):
        res = User.get_by_attr(results=InfoForProject.RESILTS)
        assert False