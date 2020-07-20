from flask import Flask, url_for

app = Flask(__name__)


@app.route("/index")
def index():
    return "index"

@app.route("/user/<username>")
def user_username(username):
    return username

@app.route("/url_for")
def URL_FOR():
    print(url_for("index")) # /index
    print(url_for("index",age=18,username="bingo")) # /index?age=18&username=bingo
    print(url_for("user_username",username="biningo")) # /user/biningo
    return "OK"

if __name__ == '__main__':
    app.run(port=8080,debug=True)