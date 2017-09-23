from html.parser import HTMLParser
from pl.weakpoint.surveyreader.builder.surveyListBuilder import SurveyListBuilder


class SurveyListParser(HTMLParser):

    TEXT_TO_REPLACE = 'Ankieta wypełniona'
    result = []
    ol_tag_found = False
    li_tag_found = False
    a_tag_found = False
    span_tag_found = False

    def __init__(self):
        super().__init__()
        self.ol_tag_found = False
        self.li_tag_found = False
        self.a_tag_found = False
        self.span_tag_found = False
        self.builder = None
        self.info = ""
        self.link = ""

    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)
        if tag == "ol":
            self.ol_tag_found = True

        if tag == 'li' and self.ol_tag_found:
            self.li_tag_found = True
            self.builder = SurveyListBuilder()
            return

        if tag == 'a' and self.li_tag_found:
            self.a_tag_found = True
            self.link = ""
            for attr in attrs:
                if attr[0] == 'href':
                    if self.a_tag_found:
                        self.link = attr[1]
                        return

        if tag == 'span' and self.a_tag_found:
            self.span_tag_found = True
            self.info = ""
            return

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)
        if tag == "ol":
            self.ol_tag_found = False
            return

        if tag == 'li' and self.ol_tag_found:
            self.li_tag_found = False
            if self.builder is not None:
                self.result.append(self.builder.build())
                return

        if tag == 'a' and self.li_tag_found:
            self.a_tag_found = False
            self.builder.set_link(self.link)
            return

        if tag == 'span' and self.a_tag_found:
            self.span_tag_found = False
            self.info = self.info.replace(self.TEXT_TO_REPLACE, "")
            self.builder.set_info(self.info.strip())
            return

    def handle_data(self, data):
        if self.span_tag_found:
            self.info += data

    def parse_surveys_list(self, html):
        self.feed(html)
        return self.result
