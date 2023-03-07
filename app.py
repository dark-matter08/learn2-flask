from flask import Flask, request, jsonify

app = Flask(__name__)


def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("books.sqlite")
    except sqlite3.error as e:
        print(e)

    return conn


@app.route('/')
def index():
    return '<h1>Hello Welome to my data stuff</h1>'


@app.route('/<name>')
def print_name(name):
    return 'Hi, Mr. {}'.format(name)


@app.route('/books', methods=['GET', 'POST'])
def books():
    conn = db_connection()
    cur = conn.cursor()
    if request.method == 'GET':
        cursor = conn.execute("SELECT * FROM book")
        books = [
            dict(id=row[0], author=row[1], language=row[2], title=row[3])
            for row in cursor.fetchall()
        ]
        
        if books is not None:
            return jsonify(books)

        else:
            'Nothing Found', 404

    if request.method == 'POST':
        print(request.form)
        new_author = request.form['author']
        new_language = request.form['language']
        new_title = request.form['title']
        
        sql = """INSERT INTO book (author, language, title) VALUES (?, ?, ?)"""
        cursor = cur.execute(sql, (new_author, new_language, new_title))
        conn.commit()
        
        return f"Book with the id: {cursor.lastrowid} created successfully", 201


@app.route('/book/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_book(id):
    if request.method == 'GET':
        pass

    if request.method == 'PUT':
        pass

    if request.method == 'DELETE':
        pass


if __name__ == '__main__':
    app.run(debug=True)
