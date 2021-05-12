from flask import Flask
from flask import send_file
from jinja2 import Template
from flask import render_template, url_for, request, redirect, flash
import csv
from questionnaire import *
from flask import flash, render_template, request, redirect
from importCSV import *
import os.path
from TeamSorting import *


app = Flask(__name__)
application = app

@app.route('/')
def index():
    return render_template("index.html")
# homepage simple render of template

@app.route('/home')
def home():
    return render_template("index.html")
# homepage simple render of template

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
#the above method takes the question dictionary and breaks it down into two arrays that can be manipulated with jinja in the web page to display the questions
#and the answer options

# https://stackoverflow.com/questions/27379486/retrieving-html-form-data-and-storing-in-csv-with-flask-python?answertab=votes#tab-top reference for function
@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method=='POST':
        stud_no=request.form["stud_no"]
        stud_email=request.form["stud_email"]
        first_choice=request.form["0"]
        second_choice=request.form["1"]
        third_choice=request.form["2"]
        extrainfo=request.form['extrainfo']
        file_exists=os.path.isfile("results.csv")
        with open('results.csv', 'a') as inFile:
            fieldnames=['Student Number','Student Email','Program Skills', 'Degree', 'Lang. Pref', 'Extra Information']
            writer= csv.DictWriter(inFile, fieldnames=fieldnames, extrasaction='ignore')
            if not file_exists:
                writer.writeheader()
            writer.writerow({'Student Number': stud_no, 'Student Email': stud_email, 'Program Skills': first_choice, 'Degree': second_choice, 'Lang. Pref': third_choice, 'Extra Information': extrainfo})
    return render_template('results.html')

# the method above defines the fields  of the csv file from the names of the html elements in the form, there is then a method to open and write to a csv file with those items.
# to ensure that the header is only written once there is a check to see if the file has been created yet, if it hasn't then when the new file opens it writes  the first row with the header
# if there are already records there it doesn't add additional field names just the data


@app.route('/staff', methods=['GET', 'POST'])
def staff():
    return render_template('staff_portal.html')

#simple render of staff portal

@app.route('/studentportal')
def studentportal():
    return render_template('student_portal.html')
#simple render of student portal

@app.route('/getCSV')
def getCSV():
    file_exists = os.path.isfile("results.csv")
    if file_exists:
        return send_file('results.csv', mimetype='text/csv', attachment_filename="results.csv", as_attachment=True)
    else:
        return render_template('no_results.html')

#returns the csv file to download. Checks first to make sure it exists. Error message if it doesn't. Copies of the csv file
#seem to stay in the browser cache even if it has been deleted from the app so sometimes browser downloads the cached version
#solved by clearing cache

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

#for viewing the questionnaire results as a table the csv file is broken down into component arrays. If the file doesn't
#exist a page telling them that no results have been received yet is presented.

@app.route('/purge')
def purge():
    os.remove("results.csv")
    message="Success! Results purged."
    return render_template("staff_portal.html",  message = message)
#completely wipes results csv from the system allowing new file to be created the next time a student triggers it
#by completing a questionnaire

@app.route('/staffques', methods=['GET', 'POST'])
def staffques():
    if request.method=='POST':
        m =int(request.form["deg_weighting"])
        n =int(request.form["prog_weighting"])
        sz = int(request.form["team_size"])
    file_exists = os.path.isfile("results.csv")
    if file_exists:
        res = importCSV('results.csv')
        stud_ans = res.getcsvs('results.csv')
        number_records = len(stud_ans)
        ts=TeamSorting()

        teams = ts.makeArray(ansarray = stud_ans, m=m, n=n, sz=sz)
    else:
        return render_template('no_results.html')
    teams_exist = os.path.isfile("teams.csv")
    with open('teams.csv', 'w' ) as inFile:

        fieldnames = ['Student Number', 'Student Email','Lang Pref', 'Team Number', 'Extra Info']
        writer = csv.DictWriter(inFile, fieldnames=fieldnames, extrasaction='ignore')
        if not teams_exist:
            writer.writeheader()
        for item in teams:
            writer.writerow({ 'Student Number': item[0], 'Student Email': item[1], 'Lang Pref': item[2], 'Team Number': item[3], 'Extra Info': item[4]})
        return render_template('team_results.html',  teams=teams, stud_ans = stud_ans, number_records= number_records, sz=sz,  m=m, n = n)
    # else:
    #     return render_template('no_results.html')

# the above method is for taking the results and putting it into an array of arrays which can then be operated on by TeamSorting()
@app.route('/team_sort', methods=['GET', 'POST'])
def team_sort():
    file_exists = os.path.isfile("results.csv")
    if file_exists:
        res = importCSV('results.csv')
        stud_ans = res.getcsvs('results.csv')
        number_records = len(stud_ans)
        return render_template('team_sort.html',  stud_ans=stud_ans, number_records=number_records)
    else:
        return render_template('no_results.html')


@app.route('/team_download')
def team_download():
    file_exists = os.path.isfile('teams.csv')
    if file_exists:
        return send_file('teams.csv', mimetype='text/csv', attachment_filename="teams.csv", as_attachment=True)
    else:
        return render_template('no_results.html')



if __name__ == "__main__":
    app.run(debug=True)




