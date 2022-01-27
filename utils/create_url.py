from config.info_for_api import InfoForProject
from config.url import Url


class CreateUrl():

    @staticmethod
    def get_url(params: dict):
        url = Url.API_URL.format(InfoForProject.API_VERSION)
        for key, val in params.items():
            url = url + key + '=' + str(val) + '&'
        return url[:-1]
