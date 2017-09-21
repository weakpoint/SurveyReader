from pl.weakpoint.surveyreader.communication.siteConnector import SiteConnector

connector = SiteConnector()
connector.connect()
page = connector.read_surveys_page()
print(page)
connector.disconnect()
