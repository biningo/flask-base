from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hello/<name>")
def hello(name=None):
    # flask会去寻找 templates目录下的文件 并进行渲染 name可以做html里面使用  {{name}}
    return render_template("hello.html",name=name)

if __name__ == '__main__':
    app.run(port=8080,debug=True)