from flask import Blueprint

goods = Blueprint('goods',__name__)

@goods.route('/index')
def index():
    return "goods"