from flask import Blueprint

books = Blueprint('books',__name__)

@books.route('/index')
def index():
    return "books"