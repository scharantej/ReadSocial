
# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for

# Create a Flask app
app = Flask(__name__)

# Books database (temporary, should be replaced with a database)
books = [
    {
        'id': 1,
        'title': 'The Hitchhiker\'s Guide to the Galaxy',
        'author': 'Douglas Adams',
        'genre': 'Science Fiction',
        'summary': 'A hilarious and thought-provoking novel about a human who travels through space with his alien friend.',
        'comments': []
    },
    {
        'id': 2,
        'title': 'The Lord of the Rings',
        'author': 'J.R.R. Tolkien',
        'genre': 'Fantasy',
        'summary': 'An epic fantasy novel that follows the journey of a group of hobbits as they try to destroy the One Ring.',
        'comments': []
    },
]


@app.route('/')
def index():
    """
    Render the landing page, which displays a list of books.

    Returns:
        The landing page HTML.
    """
    return render_template('index.html', books=books)


@app.route('/book/<int:book_id>')
def book_details(book_id):
    """
    Render the details page for a specific book, including comments.

    Args:
        book_id (int): The ID of the book to display.

    Returns:
        The book details page HTML.
    """
    book = next(book for book in books if book['id'] == book_id)
    return render_template('book_details.html', book=book)


@app.route('/search', methods=['POST'])
def search():
    """
    Search for books by title or author.

    Returns:
        The landing page HTML with filtered books.
    """
    query = request.form.get('query')
    filtered_books = [book for book in books if query in book['title'] or query in book['author']]
    return render_template('index.html', books=filtered_books)


@app.route('/add_comment', methods=['POST'])
def add_comment():
    """
    Add a new comment to a book.

    Returns:
        The book details page HTML with the new comment added.
    """
    book_id = request.form.get('book_id')
    comment = request.form.get('comment')
    book = next(book for book in books if book['id'] == int(book_id))
    book['comments'].append(comment)
    return redirect(url_for('book_details', book_id=book['id']))


if __name__ == "__main__":
    app.run(debug=True)
