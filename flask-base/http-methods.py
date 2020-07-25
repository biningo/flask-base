from flask import Flask, request

app = Flask(__name__)

#OPTIONS 不会进过这个方法  flask自动实现了方法 直接返回OPTIONS的响应
@app.route("/ping",methods=['get','POST']) #大写小写都可
def test():
    print(type(request.method))
    return request.method  # GET POST DELETE

if __name__ == '__main__':
    app.run(port=8080)