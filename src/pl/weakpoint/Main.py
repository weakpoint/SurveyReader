from pl.weakpoint.surveyreader.builder.surveyEntryBuilder import SurveyFileEntryBuilder
from pl.weakpoint.surveyreader.communication.siteConnector import SiteConnector
from pl.weakpoint.surveyreader.reader.parser.surveyListParser import SurveyListParser
from pl.weakpoint.surveyreader.reader.parser.surveyParser import SurveyParser
from pl.weakpoint.surveyreader.write.csvFileWriter import CSVFileWriter

connector = None
writer = None
try:
    connector = SiteConnector()
    connector.connect()
    page = connector.read_surveys_list_main_page()
    list_of_links = SurveyListParser().parse_surveys_list(page)
    writer = CSVFileWriter("D:\\test.csv")
    for link in list_of_links:
        survey_page = connector.get_survey_page(link.href)
        answers = SurveyParser().parse_survey(survey_page)
        line = SurveyFileEntryBuilder().set_answers_list(answers).build()
        writer.write(line)
        print(line)
        print(" ==> ", len(answers))
finally:
    if connector is not None:
        connector.disconnect()

    if writer is not None:
        writer.close()
