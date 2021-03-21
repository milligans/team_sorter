from flask import Flask
from flask import send_file
from jinja2 import Template
from flask import render_template, url_for, request, redirect, flash
import csv
from questionnaire import *
from flask import flash, render_template, request, redirect
from importCSV import *
import os.path

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
        file_exists=os.path.isfile("results.csv")
        with open('results.csv', 'a') as inFile:
            fieldnames=['Student Number','Program Skills', 'Degree', 'Lang. Pref', 'Extra Information']
            writer= csv.DictWriter(inFile, fieldnames=fieldnames, extrasaction='ignore')
            if not file_exists:
                writer.writeheader()
            writer.writerow({'Student Number': stud_no, 'Program Skills': first_choice, 'Degree': second_choice, 'Lang. Pref': third_choice, 'Extra Information': extrainfo})
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
    file_exists = os.path.isfile(results.csv)
    if file_exists:
        return send_file('results.csv', mimetype='text/csv', attachment_filename="results.csv", as_attachment=True)
    else:
        message="The file doesn't exist yet"
        return message

@app.route('/view_quest')
def view_quest():
    file_exists = os.path.isfile("results.csv")
    if file_exists:
        res=importCSV('results.csv')
        stud_ans = res.getcsvs('results.csv')
        number_records=len(stud_ans)
        return render_template('view_quest.html', stud_ans=stud_ans, number_records=number_records)
    else:
        return render_template('no_results.html')

@app.route('/purge')
def purge():
    os.remove("results.csv")
    message="Success! Results purged."
    return render_template("view_quest.html",  message = message)

if __name__ == "__main__":
    app.run(debug=True)




