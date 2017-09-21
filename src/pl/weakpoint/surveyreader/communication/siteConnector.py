import requests
from pl.weakpoint.surveyreader.configuration.config import Config


class SiteConnector:

    _payload = {}

    def __init__(self):
        name = Config.name
        password = Config.password

        if name is not "" and password is not "":
            self._payload = {'name': name, 'password': password}

        self._url = 'http://www.ankieter.pl/logowanie/loguj/'
        self._session = requests.session()

    def connect(self):
        self._session.post(self._url, data=self._payload)

    def disconnect(self):
        self._session.close()

    def read_surveys_page(self):
        request = self._session.get('http://www.ankieter.pl/wyniki/pojedyncze/id/17660/')
        return request.text




