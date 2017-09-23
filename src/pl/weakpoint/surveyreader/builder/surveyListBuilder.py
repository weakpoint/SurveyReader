from pl.weakpoint.surveyreader.model.surveyListModel import SurveyListModel


class SurveyListBuilder:

    _info = ""
    _link = ""

    def __init__(self):
        pass

    def build(self):
        if len(self._info) > 0 and len(self._link) > 0:
            return SurveyListModel(self._info, self._link)
        else:
            return None

    def set_link(self, link):
        self._link = link

    def set_info(self, info):
        self._info = info
