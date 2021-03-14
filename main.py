from questionnaire import Questionnaire


student_skills = Questionnaire()

student_skills.build_questions()

student_questions = student_skills.quest_items
student_answers = student_skills.answers
print(len(student_questions))


for item in range(len(student_questions)):
    print(student_questions[item])
    print("Please select your answer from the list below: ")
    for answer in student_answers[item]:
        print(answer)


