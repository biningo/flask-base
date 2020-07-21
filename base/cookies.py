from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/cookie")
def Cookie():
    print(request.cookies)
    return request.cookies

@app.route("/set_cookie")
def set_cookie():
    resp = make_response()
    resp.set_cookie("username","bingo") #et cookie at response header
    return resp

if __name__ == '__main__':
    app.run(port=8080,debug=True)