from pl.weakpoint.surveyreader.builder.surveyFileEntryBuilder import SurveyFileEntryBuilder
from pl.weakpoint.surveyreader.communication.siteConnector import SiteConnector
from pl.weakpoint.surveyreader.reader.parser.surveyListParser import SurveyListParser
from pl.weakpoint.surveyreader.reader.parser.surveyParser import SurveyParser
from pl.weakpoint.surveyreader.write.csvFileWriter import CSVFileWriter
from datetime import datetime

START_DATE = datetime.strptime("08.08.2017", '%d.%m.%Y')
connector = None
writer = None
valid = 0
try:
    connector = SiteConnector()
    connector.connect()
    page = connector.read_surveys_list_main_page()
    list_of_links = SurveyListParser().parse_surveys_list(page)
    writer = CSVFileWriter("D:\\test.csv")
    for link in list_of_links:
        print("Link time: " + link.date)
        datetime_object = datetime.strptime(link.date, '%d.%m.%Y, %I:%M')
        if START_DATE <= datetime_object:
            survey_page = connector.get_survey_page(link.href)
            answers = SurveyParser().parse_survey(survey_page)
            line = SurveyFileEntryBuilder().set_answers_list(answers).build()
            writer.write(line)
            print(line)
            valid += 1
    print("All links: ", len(list_of_links))
    print("All VALID links: ", valid)
finally:
    if connector is not None:
        connector.disconnect()

    if writer is not None:
        writer.close()
