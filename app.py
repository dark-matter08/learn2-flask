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
        for book in book_list:
            if book['id'] == id:
                return jsonify(book)
            pass

    if request.method == 'PUT':
        for book in book_list:
            if book['id'] == id:
                book['author'] = request.form['author']
                book['language'] = request.form['language']
                book['title'] = request.form['title']

                updated_book = {
                    'id': id,
                    'author': book['author'],
                    'language': book['language'],
                    'title': book['title']
                }

                return jsonify(updated_book)

    if request.method == 'DELETE':
        for index, book in enumerate(book_list):
            if book['id'] == id:
                book_list.pop(index)

                return jsonify(book_list)


if __name__ == '__main__':
    app.run(debug=True)
