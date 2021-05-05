import mysql.connector
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

app = Flask(__name__)
currentUserId = -1

def get_db_connection():
    # TODO: Connect to GCP
    MyPassword = "r3d570n3"
    MyUser = "root"
    MyHost = "35.193.60.27"
    MyDatabase = "jain322"

    cnx = mysql.connector.connect(user='root', password='12345', host='localhost', database='cs348proj')

    return cnx

@app.route('/')
def index():
    # TODO: Call get_db_connection and start connection
    # TODO: Fetch books read and books to be read from user
    return render_template('index.html')

@app.route('/home')
def home():
    global currentUserId
    print("HOME: " + str(currentUserId))
    cnx = get_db_connection()
    query = "select * from book natural join reviewrel natural join review where reader_id = " + str(currentUserId) + ";"
    cursor = cnx.cursor()
    cursor.execute(query)
    posts = []
    print("HOME")
    for (review_id, bookid, title, isbn, published_date, publisher, reader_id, rating, review) in cursor:
        posts.append([bookid, title, isbn, published_date, publisher, review])


    cursor.close()
    cnx.close()
    return render_template('home.html', posts=posts)

@app.route('/home', methods = ['POST'])
def login_verification():
    # TODO if request.form length = 2 then check login against database
    # else create new person on database
    global currentUserId
    cnx = get_db_connection()
    cursor = cnx.cursor()
    verifiedflag = False
    if (len(request.form) == 2): 
        #existing user
        #check login details with users database
        newemail = request.form['email']
        newpassword = request.form['password']
        query = "SELECT * FROM reader WHERE email = \"" + newemail + "\";"
        cursor.execute(query)
        result = cursor.fetchall()
        print(type(result))
        if len(result) == 0:
            return render_template('index.html')
        else:
            currentUserId = result[0][0]
            # currentUserId = result[0]["reader_id"]
            # print(currentUserId)
    else:
        #add new user
        firstname = request.form['fname']
        email = request.form['email']
        lastname = request.form['lname']
        password = request.form['password']
    
        # add new user to database
    print("reader is " + str(currentUserId))
    # only return this if login is verified OR if signup
    cursor.close()
    cnx.close()
    return home()

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/add', methods = ['POST'])
def add_book():
    global currentUserId
    bookName = request.form['bookName']
    bookIsbn = request.form['bookIsbn']
    bookDate = request.form['bookDate']
    bookPublisher = request.form['bookPublisher']
    bookReview = request.form['bookReview']
    bookRating = 5
    cnx = get_db_connection()
    cursor = cnx.cursor()

    add_book_query = "INSERT INTO book "\
        "(title, isbn, published_date, publisher) "\
        "VALUES (%s, %s, %s, %s)"
    book_data = (bookName, bookIsbn, bookDate, bookPublisher)
    cursor.execute(add_book_query, book_data)

    get_book_id = "SELECT book_id FROM book where isbn = " + bookIsbn + ";"
    cursor.execute(get_book_id)
    result = cursor.fetchall()
    bookId = result[0][0]

    add_review = "INSERT INTO review "\
        "(rating, review) "\
        "VALUES (%s, %s)"
    review_data = (bookRating, bookReview)
    cursor.execute(add_review, review_data)

    get_review_id = "SELECT review_id FROM review where review = \"" + bookReview + "\";"
    cursor.execute(get_review_id)
    result = cursor.fetchall()
    reviewId = result[0][0]

    add_review_rel = "INSERT INTO reviewrel "\
        "(reader_id, book_id, review_id) "\
        "VALUES (%s, %s, %s)"
    review_rel_data = (currentUserId, bookId, reviewId)
    cursor.execute(add_review_rel, review_rel_data)
    cnx.commit()

    cursor.close()
    cnx.close()
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
