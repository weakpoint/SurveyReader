from pl.weakpoint.surveyreader.builder.surveyListBuilder import SurveyListBuilder
import re

from pl.weakpoint.surveyreader.reader.parser.surveyListParser import SurveyListParser


class SurveyResultListReader:

    def __init__(self):
        pass

    def read(self, html):
        result = []
        survey_lists_html = self.__find_surveys_list(html)
        splitted_links = self.split_links_html_entries(survey_lists_html)

        for link in splitted_links:
            model = SurveyListBuilder().set_html(link).build()
            if model is not None:
                result.append(model)
        return result

    def __find_surveys_list(self, html):
        idx_print = html.find("/wyniki/pobierzAnkiety")

        if idx_print > -1:
            print(html)
            parser = SurveyListParser()
            parser.feed(html)

            # p.mach(s).groups()
            # p.search(s).groups()
            # p.findall(s)
            idx_ol_start = html.find("<ol>", idx_print)
            idx_ol_stop = html.find("</ol>", idx_ol_start)

            if idx_ol_stop > -1:
                return html[idx_ol_start:idx_ol_stop]
        return None

    def split_links_html_entries(self, list_html):
        if len(list_html) != 0:
            splitted_html = list_html.split("<a href=")
            return splitted_html
