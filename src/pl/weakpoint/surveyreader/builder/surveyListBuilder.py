from pl.weakpoint.surveyreader.model.surveyListModel import SurveyListModel


class SurveyListBuilder:

    LINK_START_TAG = '"'
    LINK_END_TAG = '</a>'
    INFO_START_TEXT = 'Ankieta wypełniona'
    INFO_END_TEXT = '</span>'
    _info = ""
    _link = ""

    def __init__(self):
        pass

    def build(self):
        if len(self._info) > 0 and len(self._link) > 0:
            return SurveyListModel(self._info, self._link)
        else:
            return None

    def set_html(self, html):
        if len(html) > 0:
            link_start_idx = html.find(self.LINK_START_TAG)
            link_end_idx = html.find(self.LINK_END_TAG, link_start_idx)

            if link_start_idx > -1:
                link = html[link_start_idx:link_end_idx]
                self.__set_link(link)
                self.__set_info(link)
        return self

    def __set_info(self, link_html):
        if len(link_html) > 0:
            info_start_idx = link_html.find(self.INFO_START_TEXT) + len(self.INFO_START_TEXT)
            info_end_idx = link_html.find(self.INFO_END_TEXT, info_start_idx)
            self._info = link_html[info_start_idx:info_end_idx].strip()

    def __set_link(self, link_html):
        if len(link_html) > 0:
            link_start_idx = link_html.find("\"") + 1
            link_end_idx = link_html.find("\"", link_start_idx)
            self._link = link_html[link_start_idx:link_end_idx]