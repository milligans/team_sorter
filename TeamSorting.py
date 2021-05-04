import numpy as np

class TeamSorting():

   def makeArray(self, ansarray, m, n,sz):
        team_select =[]
        j = 0
        english_team=[]
        welsh_team=[]
        # n = 1
        # m = 10
        # this number 'n' will be used for the weighting factor
        while j < len(ansarray):
            for i in ansarray:
                if i != ansarray[0]:
                    if i[4] == "Welsh":
                        i[4] = False
                    elif i[4] == "English":
                        i[4] = True
                    if i[2] == "High - familiar with more than one language":

                        i[2]=3 * n

                    elif i[2] == "Medium - some experience":
                        i[2]=2 * n

                    elif i[2] =="Low - no or very little":
                        i[2] =1 *n
                    if i[3] == "other":
                        i[3] =1 * m
                    elif i[3] == "BEng":
                        i[3] =2 * m
                    elif i[3] == "BSc":
                        i[3] =2 * m
                    elif i[3] == "LLB":
                        i[3] =1 * m
                    elif i[3] == "BA":
                        i[3] = 1 * m
                    composite = i[3] * i[2]
                    i[3] = composite
                    # the composite score is the degree score multiplied by the programming skills score which have already been weighted

                    team_select.append(i)
                    j = j + 1

        # to split into composite score first

        team_select.sort(key = lambda x: x[3])
        team_select.sort(key=lambda x: x[4])
        # then split on language





        return team_select



