from flask import Flask, render_template, request

import requests
from flask_wtf import *
from questionnaire import Questionnaire
from flask import flash, render_template, request, redirect


posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()



app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")



@app.route('/students', methods = ['GET', 'POST'])
def students():
    student_responses = []
    student_skills = Questionnaire()
    student_skills.build_questions()
    student_questions = student_skills.quest_items
    student_answers = student_skills.answers
    number_questions=len(student_questions)
    return render_template("studentques.html", student_questions=student_questions, student_answers=student_answers, student_responses=student_responses, number_questions= number_questions)

# @app.route('/results')
# def search_results(search):
#     results = []
#     search_string = search.data['search']
#     if search.data['search'] == '':
#         qry = db_session.query(Album)
#         results = qry.all()
#     if not results:
#         flash('No results found!')
#         return redirect('/')
#     else:
#         # display results
#         return render_template('results.html', results=results)
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



