from pl.weakpoint.surveyreader.communication.siteConnector import SiteConnector
from pl.weakpoint.surveyreader.reader.parser.surveyListParser import SurveyListParser
from pl.weakpoint.surveyreader.reader.parser.surveyParser import SurveyParser

connector = None
try:
    connector = SiteConnector()
    connector.connect()
    page = connector.read_surveys_list_main_page()
    list_of_links = SurveyListParser().parse_surveys_list(page)
    for i,link in enumerate(list_of_links):
        survey_page = connector.get_survey_page(link.href)
        print(SurveyParser().parse_survey(survey_page))
finally:
    if connector is not None:
        connector.disconnect()
