from flask import Flask
from flask import send_file
from jinja2 import Template
from flask import render_template, url_for, request, redirect, flash
import csv
from questionnaire import *
from flask import flash, render_template, request, redirect


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/home')
def home():
    return render_template("index.html")


@app.route('/students', methods=['GET', 'POST'] )
def students():

    student_responses = []
    student_skills = Questionnaire()
    student_skills.build_questions(QUEST_DICTIONARY)
    student_questions = student_skills.quest_items
    student_answers = student_skills.answers
    number_questions=len(student_questions)
    number_answers=len(student_answers)

    return render_template("studentques.html", students= students, student_questions=student_questions, student_answers=student_answers, student_responses=student_responses, number_questions= number_questions, number_answers=number_answers)

# https://stackoverflow.com/questions/27379486/retrieving-html-form-data-and-storing-in-csv-with-flask-python?answertab=votes#tab-top
@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method=='POST':
        stud_no=request.form["stud_no"]
        first_choice=request.form["0"]
        second_choice=request.form["1"]
        third_choice=request.form["2"]
        extrainfo=request.form['extrainfo']
        with open('results.csv', 'a') as inFile:
            fieldnames=['Student Number','Question One', 'Question Two', 'Question Three', 'Extra Information']
            writer= csv.DictWriter(inFile, fieldnames=fieldnames, extrasaction='ignore')
            # writer.writeheader()
            writer.writerow({'Student Number': stud_no, 'Question One': first_choice, 'Question Two': second_choice, 'Question Three': third_choice, 'Extra Information': extrainfo})
    return render_template('results.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/staff', methods=['GET', 'POST'])
def staff():
    return render_template('staff_portal.html')

@app.route('/getCSV')
def getCSV():
    return send_file('results.csv', mimetype='text/csv', attachment_filename="results.csv", as_attachment=True)

@app.route('/view_quest')
def view_quest():
    return render_template('view_quest.html')

if __name__ == "__main__":
    app.run(debug=True)




