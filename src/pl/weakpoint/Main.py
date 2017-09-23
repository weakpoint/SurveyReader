from pl.weakpoint.surveyreader.builder.surveyEntryBuilder import SurveyFileEntryBuilder
from pl.weakpoint.surveyreader.communication.siteConnector import SiteConnector
from pl.weakpoint.surveyreader.reader.parser.surveyListParser import SurveyListParser
from pl.weakpoint.surveyreader.reader.parser.surveyParser import SurveyParser

connector = None
try:
    connector = SiteConnector()
    connector.connect()
    page = connector.read_surveys_list_main_page()
    list_of_links = SurveyListParser().parse_surveys_list(page)
    for link in list_of_links:
        survey_page = connector.get_survey_page(link.href)
        answers = SurveyParser().parse_survey(survey_page)
        print(SurveyFileEntryBuilder().set_answers_list(answers).build())
        print(" ==> ", len(answers))
finally:
    if connector is not None:
        connector.disconnect()
