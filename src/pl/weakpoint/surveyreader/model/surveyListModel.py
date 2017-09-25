class SurveyListModel:

    date = ""
    href = ""

    def __init__(self, date, href):
        self.date = date
        self.href = href

    def __str__(self):
        return "date: " + self.date + "; href: " + self.href

    def __repr__(self):
        return self.__str__()
