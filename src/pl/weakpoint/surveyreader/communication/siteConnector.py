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

    def read_surveys_list_main_page(self):
        return self.get_survey_page('/wyniki/pojedyncze/id/17660/')

    def get_survey_page(self, url):
        request = self._session.get('http://www.ankieter.pl' + url)
        return request.text




