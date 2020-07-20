from flask import Flask
app = Flask(__name__)

@app.route("/ping")
def ping():
    return "Pong"

@app.route("/")
def hello():
    return "hello,world"



if __name__ == '__main__':
    app.run(port="8080",debug=True) #设置debug可以动态刷新更改
