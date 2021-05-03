class TeamSorting():

   def makeArray(self, ansarray, m, n):
        team_select =[]
        j = 0
        # n = 1
        # m = 10
        # this number 'n' will be used for the weighting factor
        while j < len(ansarray):
            for i in ansarray:
                if i != ansarray[0]:
                    if i[4] == "Welsh":
                        i[4] = False
                    else:
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

                    team_select.append(i)
                    j = j + 1
        return team_select
