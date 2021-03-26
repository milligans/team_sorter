QUEST_DICTIONARY = {"What is your prior level of programming?": ("High - familiar with more than one language", "Medium - some experience", "Low - no or very little"),
                    "What is your undergraduate degree type?": ("BSc", "BEng", "BA","LLB", "other"),
                    "Which language is preferred language?": ("Welsh", "English")
                    }


# the above dictionary is a constant that can be altered when extra questions need to be added, or the text changed. Changing the text from here changes
# it everywhere - however the field names in the wsgi route for the results page rely on the field names matching the questions so if the questions
# are altered in quantity or question type the fields need to be altered in results() function in the wsgi file


class Questionnaire():




    def build_questions(self, QUEST_DICTIONARY):
        self.quest_items = list(QUEST_DICTIONARY.keys())
        self.answers = list(QUEST_DICTIONARY.values())




    # def build_confirmation(self, array):
