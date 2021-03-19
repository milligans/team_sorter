from flask import Flask, render_template, request
import csv
import requests
from flask_wtf import *
from questionnaire import Questionnaire
from flask import flash, render_template, request, redirect






app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")



@app.route('/students', methods=['GET', 'POST'] )
def students():

    student_responses = []
    student_skills = Questionnaire()
    student_skills.build_questions()
    student_questions = student_skills.quest_items
    student_answers = student_skills.answers
    number_questions=len(student_questions)
    number_answers=len(student_answers)

    return render_template("studentques.html", students= students, student_questions=student_questions, student_answers=student_answers, student_responses=student_responses, number_questions= number_questions, number_answers=number_answers)

# https://stackoverflow.com/questions/27379486/retrieving-html-form-data-and-storing-in-csv-with-flask-python?answertab=votes#tab-top
@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method=='POST':
        first_choice=request.form["0"]
        second_choice=request.form["1"]
        third_choice=request.form["2"]
        extrainfo=request.form['extrainfo']
        with open('results.csv', 'w') as inFile:
            fieldnames=['Question One', 'Question Two', 'Question Three', 'Extra Information']
            writer= csv.DictWriter(inFile, fieldnames=fieldnames, delimiter = ';', extrasaction='ignore')
            writer.writerow({'Question One': first_choice, 'Question Two': second_choice, 'Question Three': third_choice, 'Extra Information': extrainfo})
    return render_template('results.html')
#
#
#
# @app.route("/post/<int:index>")
# def show_post(index):
#      requested_post = None
#      for blog_post in posts:
#          if blog_post["id"] == index:
#              requested_post = blog_post
#      return render_template("post.html", post=requested_post)
#
#
# @app.route("/about")
# def about():
#     return render_template("about.html")
#
#
# @app.route("/contact")
# def contact():
#     return render_template("contact.html")
#
# @app.route("/form-entry", methods=["POST"])
# def receive_data():
#     name = request.form["name"]
#     email = request.form["email"]
#     message = request.form["message"]
#     return render_template("form-entry.html", email=email, name=name, message=message)
#
#



if __name__ == "__main__":
    app.run(debug=True)




