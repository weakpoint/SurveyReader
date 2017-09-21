class SurveyResultListReader:

    def __init__(self):
        pass

    def read(self, html):
        result = []
        surveyListsHtml = findSurveysList(html)

        return result

    def findSurveysList(self, html):
        idxPrint = html.find("/wyniki/pobierzAnkiety")

        if idxPrint > -1:
            idx_ol_start = html.find("<ol>", idxPrint)
            idx_ol_stop = html.find("</ol>", idx_ol_start)

            if idx_ol_stop > -1:
                return html[idx_ol_start:idx_ol_stop]
        return None
