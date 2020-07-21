from flask import Flask, make_response, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return "404", 404  # 第二个参数是状态码 如果返回一个字符串 默认会转化为body里的str


# make_response 自己定义response
@app.route("/r1")
def r1():
    resp = make_response("ok")
    resp.headers['cookie'] = "name=bingo,age=18"
    resp.headers['content-type'] = 'application/json; charset=utf-8'
    return resp


# 返回json数据
@app.route("/r2")
def r2():
    return {
        "name": "bingo",
        "age": 18
    }

@app.route("/r4")
def r4():
    return {
        "name":"bingo",
        "hobby":["running","basketball"],
    }


@app.route("/r3")
def r3():
    d1 = {"name": "bingo1", "age": 18}
    d2 = {"name":"bingo2","age":19}
    arr = [d1,d2]
    return jsonify(arr) #除了单个字典，其他都要用这个函数包裹,比如数组 对象等

class Stu():
    hobby=[]
    def __init__(self,name,age):
        self.name =name
        self.age = age

    def keys(self):
        return ('name', 'age')

    def __getitem__(self, item):
        return getattr(self, item)


@app.route("/r5")
def r5():
    s = Stu("bingo",18)
    print(s.__dict__) #只会返回self的字段
    s = dict(s) #根据keys 和getitem函数获取值
    return jsonify(s)




if __name__ == '__main__':
    app.run(port=8000, debug=True)
