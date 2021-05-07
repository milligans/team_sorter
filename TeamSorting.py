

class TeamSorting():

   def makeArray(self, ansarray, m, n,sz):
        team_select =[]
        english_team=[]
        welsh_team=[]
        cpwt=[]
        cpet=[]
        j = 0
        complete_teams=[]
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
                    # the composite score is the degree score multiplied by the
                    # programming skills score which have already been weighted

                    team_select.append(i)
                j = j + 1

        # to split into composite score first

        team_select.sort(key = lambda x: x[3])
        team_select.sort(key=lambda x: x[4])
        # then split on language

        for item in team_select:
            if item[4]:

                english_team.append(item)

            else:
                welsh_team.append(item)


        # make the team the size specified, if the remainder is less than 75% of the team size then they will be added
        # to existing teams, if more than 75% then they will make a smaller team
        if len(welsh_team) % sz == 0 or len(welsh_team) % sz < (sz * 0.75):
            number_welsh_teams = len(welsh_team) // sz
        else:
            number_welsh_teams = len(welsh_team) // sz + 1

        if len(english_team) % sz == 0 or len(english_team) % sz < (sz * 0.75):
            number_english_teams = len(english_team) // sz
        else:
            number_english_teams = len(english_team) // sz + 1

        # calculate the number of teams required and add one to mop up the excess if there is a remainder
        # print(len(welsh_team), "in the Welsh group")
        # print(number_welsh_teams, "number of Welsh Teams")
        # print(len(english_team), "number in English group")
        # print(number_english_teams, "number of English teams")

        counter = 1

        team_number = 1

        for item in welsh_team:
            cpwt.append((item[0], item[1], "Welsh language", team_number, item[5]))
            if counter == sz:
                team_number = team_number + 1
                counter = 1
            else:
                counter = counter + 1
        counter = 1
        team_number = number_welsh_teams + 1
        for item in english_team:
            cpet.append((item[0], item[1], "English Language", team_number, item[5]))
            if counter == sz:
                counter = 1
                team_number = team_number + 1
                if (team_number >= number_english_teams + number_welsh_teams):
                    team_number = number_welsh_teams + 1
                    counter = counter - 1


            else:
                counter = counter + 1

        # print(cpwt)
        # print(cpet)
        complete_teams.append(("Student Number", "Student Email", "Language Pref", "Team Number", "Extra Information"))
        for item in cpwt:
            complete_teams.append(item)

        for item in cpet:
            complete_teams.append(item)

        # print(complete_teams)

        return complete_teams



