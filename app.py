from flask import Flask, render_template

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

@app.route('/add')
def add():
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
