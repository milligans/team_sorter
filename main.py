from questionnaire import Questionnaire
from tkinter import *
from question_class import *

root=Tk()
root.title=("Student Questionnaire")
root.geometry("1000x500")
app=Question_class(root)
root.mainloop()

student_responses=[]
student_skills = Questionnaire()

student_skills.build_questions()

student_questions = student_skills.quest_items
student_answers = student_skills.answers
still_answering=True
print("\n \n *****Welcome to the student questionnaire, please answer as directed below.***** \n \n")

app.create_prog_select("Degree Subject", ["high", "low", "medium"])

while still_answering:
    for item in range(len(student_questions)):
        print(student_questions[item])
        print("Please select your answer from the list below: ")
        n=1
        for answer in student_answers[item]:
            print(f"Please select option {n}  for {answer}")
            n += 1
        item_response = input("Please input the number for your answer: ")
        # need to find a way to enforce an answer/error correct wrong answers
        student_responses.append((item, int(item_response)-1))
        print(item_response)

    for item in range(len(student_questions)):
        print("The question was ", student_questions[item])
        response_num=student_responses[item][1]
        print("Your answer was ", student_answers[item][response_num])
    answer_again = input("Are you happy with these answers? Please enter 'N' to re-enter the answers or 'Y' to continue and submit the answers.\t")
    if answer_again.lower()=="y":
        print("Answers submitted")
        still_answering=False

    else:
        print("\n \n Please answer the questions again \n\n")
        # clear the previous responses and go back to the start of the while loop
        student_responses=[]
        continue

print("Thank you for answering the questionnaire 😀")
print(student_responses)
