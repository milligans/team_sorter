from questionnaire import Questionnaire

student_responses=[]
student_skills = Questionnaire()

student_skills.build_questions()

student_questions = student_skills.quest_items
student_answers = student_skills.answers

print("\n \n *****Welcome to the student questionnaire, please answer as directed below.***** \n \n")

for item in range(len(student_questions)):
    print(student_questions[item])
    print("Please select your answer from the list below: ")
    n=1
    for answer in student_answers[item]:
        print(f"Please select option {n}  for {answer}")
        n += 1
    item_response = input("Please input the number for your answer: ")
    # need to find a way to enforce an answer/error correct wrong answers
    student_responses.append((item, int(item_response)))
    print(item_response)


# print(student_responses)
# print(student_answers)
# print(student_responses[0][1])

for item in range(len(student_questions)):
    print("The question was ", student_questions[item])
    response_num=student_responses[item][1]
    print("Your answer was ", student_answers[item][response_num-1])