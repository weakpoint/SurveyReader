from html.parser import HTMLParser


class SurveyParser(HTMLParser):
    result = []
    ol_tag_found = False
    li_tag_question_found = False
    li_tag_answer_found = False
    ul_tag_found = False
    answer = ""

    def __init__(self):
        super().__init__()
        self.ol_tag_found = False
        self.li_tag_question_found = False
        self.li_tag_answer_found = False
        self.ul_tag_found = False
        self.answer = ""
        self.result = []

    def handle_starttag(self, tag, attrs):
        if tag == 'ol':
            self.ol_tag_found = True

        if tag == 'ul' and self.li_tag_question_found:
            self.ul_tag_found = True

        if tag == 'li':
            if self.ol_tag_found and not self.ul_tag_found:
                self.li_tag_question_found = True
            elif self.ul_tag_found:
                self.li_tag_answer_found = True
            return

    def handle_endtag(self, tag):
        if tag == "ol":
            self.ol_tag_found = False
            return

        if tag == 'li':
            if self.li_tag_answer_found:
                self.li_tag_answer_found = False
            else:
                self.li_tag_question_found = False
                if self.ol_tag_found:
                    self.result.append(self.answer)
                    self.answer = ""
            return
        if tag == 'ul':
            self.ul_tag_found = False

    def handle_data(self, data):
        if self.li_tag_answer_found and self.ol_tag_found:
            self.answer = data.replace('&nbsp;', '').strip()

    def parse_survey(self, html):
        self.feed(html)
        self.close()
        return self.result
