from flask import Blueprint

tags = Blueprint('tags',__name__)

@tags.route('/index')
def index():
    return "tags"