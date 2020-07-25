import os

from flask import Flask, session, url_for
from werkzeug.exceptions import abort
from werkzeug.utils import redirect

# session每开一个窗口就是一个新的session

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/' #要用session必须设置key
@app.route("/login/<username>")
def login(username):
    session['username'] = username
    return redirect(url_for("index"))

@app.route("/")
def index():
    print(session) #SecureCookieSession
    if "username" not in session:
        abort(400)
    return "hello,"+session['username']

@app.errorhandler(400)
def error_not_login(error):
    return "sorry,not login",400


if __name__ == '__main__':
    app.run(port=8080,debug=True)