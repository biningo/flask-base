from flask import Flask, url_for
from werkzeug.exceptions import abort
from werkzeug.utils import redirect

app = Flask(__name__)

#重定向
@app.route("/")
def index():
    return redirect(url_for("login"))

@app.route("/login")
def login():
    abort(500)

@app.route("/404")
def page_not_found():
    abort(404) #不会继续执行

#错误处理函数 error参数一定要
@app.errorhandler(404)
def error_404(error):
    print(error)
    return "404 error",404 #第二个参数表示返回码

@app.errorhandler(500)
def error_500(error):
    print(error)
    return "500 error",500

if __name__ == '__main__':
    app.run(port=8080,debug=True)