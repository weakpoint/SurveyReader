class SurveyFileEntryBuilder:

    CHOOSEN = "wybrano"
    result = []
    answers = None

    def __init__(self):
        self.result = []
        self.answers = None

    def set_answers_list(self, answers):
        if answers is not None and len(answers) == 19:
            self.answers = answers

        return self

    def build(self):
        if self.answers is not None:
            self.result.extend(self.answers[0:2])
            self.result.extend(['', ''])
            self.result.extend(self.answers[2:17])
            self.result.extend(self.__manage_answer_18(self.answers[17]))
            self.result.extend(self.__manage_answer_19(self.answers[18]))
        return ';'.join(self.result)

    def __manage_answer_18(self, answer):
        return [self.add_chosen_value_when_contains('Waginalny', answer),
                self.add_chosen_value_when_contains('Oralny', answer),
                self.add_chosen_value_when_contains('Analny', answer),
                self.add_chosen_value_when_contains('Masturbacja', answer)]

    def __manage_answer_19(self, answer):
        return [self.add_chosen_value_when_contains('Waginalny', answer),
                self.add_chosen_value_when_contains('Oralny', answer),
                self.add_chosen_value_when_contains('Analny', answer)]

    def add_chosen_value_when_contains(self, value, answer):
        if answer is not None and value in answer:
            return self.CHOOSEN
        else:
            return ''
