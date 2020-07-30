from flask import Blueprint

article = Blueprint('article',__name__)

@article.route('/index')
def index():
    return "article"