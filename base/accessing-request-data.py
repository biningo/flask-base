from flask import Flask, request, Request

app = Flask(__name__)

@app.route("/info",methods=['POST','GET'])
def info():
    print(request) # Request
    print(request.path)
    print(request.method)
    if request.method=='POST':
        print(request.form) #ImmutableMultiDict   return "OK"  form|x-www-form-urlencoded
    print(request.args)  #ImmutableMultiDic    return request.args
    return request.args


if __name__ == '__main__':
    app.run(port=8080,debug=True)