from pl.weakpoint.surveyreader.communication.siteConnector import SiteConnector
from pl.weakpoint.surveyreader.reader.surveyResultListReader import SurveyResultListReader

connector = SiteConnector()
connector.connect()
page = connector.read_surveys_page()
print(page)
list_of_links = SurveyResultListReader().read(page)
print(list_of_links)
connector.disconnect()
