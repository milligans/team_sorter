from questionnaire import Questionnaire


student_skills = Questionnaire()

student_skills.build_questions()

print(student_skills.quest_items)
print(student_skills.answers)

print(len(student_skills.answers))

student_questions = student_skills.quest_items
student_answers = student_skills.answers

for item in student_questions:
    for answer in student_answers:
        for option in answer:
            print(item)
            print(option)

