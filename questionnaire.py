QUEST_DICTIONARY = {"What is your prior level of programming?": ("High - familiar with more than one language", "Medium - some experience", "Low - no or very little"),
                    "What is your undergraduate degree type?": ("BSc", "BEng", "BA","DLL", "other"),
                    "Which language is preferred language?": ("Welsh", "English", "Esperanto")
                    }




class Questionnaire():


    def __init__(self):
        self.quest_items = []
        self.answers = []



    def build_questions(self):
        self.quest_items = list(QUEST_DICTIONARY.keys())
        self.answers = list(QUEST_DICTIONARY.values())




    # def build_confirmation(self, array):
