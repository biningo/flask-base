from flask import Flask, url_for

app = Flask(__name__)

# 直接访问 /static/xxx 就可以访问 当前目录下 static/ 下的静态资源文件
# http://127.0.0.1:8080/static/yer10.png
@app.route("/ping")
def static_file():
    return url_for("static", filename="yer10.png") #/static/yer10.png

if __name__ == '__main__':
    app.run(port=8080,debug=True)