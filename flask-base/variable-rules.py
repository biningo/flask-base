from flask import Flask

# string
# int
# float
# path
# uuid

app = Flask(__name__)
#函数入参数名字必须和route定义的名字一致
@app.route("/user/<username>")
def user_username(username):
    print(type(username))
    return username

#可以指定类型
@app.route("/user/<int:id>")
def user_id(id):
    print(type(id))
    return "id+10:"+str(id+10)


if __name__ == '__main__':
    app.run(port=8080,debug=True)