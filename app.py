import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

app = Flask(__name__)

def get_db_connection():
    # TODO: Connect to GCP
    return

@app.route('/')
def index():
    # TODO: Call get_db_connection and start connection
    # TODO: Fetch books read and books to be read from user
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/home', methods = ['POST'])
def login_verification():
    # TODO if request.form length = 2 then check login against database
    # else create new person on database
    verifiedflag = False
    if (len(request.form) == 2): 
        #existing user
        #check login details with users database
        newemail = request.form['email']
        newpassword = request.form['password']
    else:
        #add new user
        firstname = request.form['fname']
        email = request.form['email']
        lastname = request.form['lname']
        password = request.form['password']
    
        # add new user to database

    # only return this if login is verified OR if signup
    return render_template('home.html')

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/add', methods = ['POST'])
def add_book():
    bookName = request.form['bookName']
    bookIsbn = request.form['bookIsbn']
    bookDate = request.form['bookDate']
    bookPublisher = request.form['bookPublisher']
    bookReview = request.form['bookReview']

    print(bookName)
    print(bookIsbn)
    print(bookDate)
    print(bookPublisher)
    print(bookReview)

    # TODO create a new database entry 

    return render_template('add.html')

@app.route('/browse')
def browse():
    return render_template('browse.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/edit')
def edit():
    return render_template('edit.html')

if __name__ == "__main__":
    app.run()
