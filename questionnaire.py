QUEST_DICTIONARY = {"What is your prior level of programming?": ("High", "Medium", "Low"),
                    "What is your undergraduate degree type?": ("BSc", "BEng", "BA", "other")}




class Questionnaire():


    def __init__(self):
        self.quest_items = []
        self.answers = []



    def build_questions(self):
        self.quest_items = list(QUEST_DICTIONARY.keys())
        self.answers = list(QUEST_DICTIONARY.values())




