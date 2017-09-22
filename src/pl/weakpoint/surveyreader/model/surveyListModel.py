class SurveyListModel:

    title = ""
    href = ""

    def __init__(self, title, href):
        self.title = title
        self.href = href

    def __str__(self):
        return "title: " + self.title + "; href: " + self.href

    def __repr__(self):
        return self.__str__()
