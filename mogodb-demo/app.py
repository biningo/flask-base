import json

from flask import Flask, jsonify, request
from pymongo import MongoClient


# collection.insert_many([
#     {'name': '小a', 'age': 10, 'hobby': ['basketball', 'running']},
#     {'name': '小b', 'age': 20, 'hobby': ['basketball', 'computer-games']}
# ])

class Student:
    def __init__(self, name='', age=None, hobby=[], email=''):
        self.name = name
        self.age = age
        self.hobby = hobby
        self.email = email
        self.deleted = False


def init_db():
    client = MongoClient("mongodb://118.178.180.115:27017")
    DB = client.bingo
    collection = DB['students']
    return collection


db = init_db()
app = Flask(__name__)


@app.route('/get/all')
def get_all():
    students = list(db.find({'deleted': 0}, {'_id': 0, 'deleted': 0}))
    return jsonify(students)


@app.route('/get/<stu_name>')
def get_by_name(stu_name):
    student = db.find_one({'name': stu_name, 'deleted': 0}, {'_id': 0, 'deleted': 0})
    return jsonify(student)


@app.route('/get/age')
def get_by_range_age():
    max_age = request.args.get('max_age')
    min_age = request.args.get('min_age')
    students = list(db.find({'age': {
        '$gt': int(min_age),
        '$lt': int(max_age)}},
        {'_id': 0, 'deleted': 0}))
    return jsonify(students)


@app.route('/get/hobby')
def get_by_hobby():
    hobby_names = request.args.getlist('name')
    print(hobby_names)
    students = list(db.find({'hobby': {'$all': hobby_names}}, {'_id': 0, 'deleted': 0}))
    return jsonify(students)


@app.route('/get/max_age')
def get_max_age():
    students = db.find({}, {'_id': 0, 'age': 1}).sort('age').sort('name')
    res = students.limit(1)[0]
    print(list(students))
    return res


@app.route('/get/sort/age')
def get_sort_age():
    key = request.args.get("key")
    key = int(key) if key else 1
    students = list(db.find({'deleted': 0}, {'_id': 0, 'deleted': 0}).sort('age', key))
    return jsonify(students)


@app.route('/delete/<stu_name>', methods=['delete'])
def delete_by_name(stu_name):
    if db.find({'name': stu_name}).count() == 0:
        return "No"
    db.update_one({'name': stu_name}, {'$set': {'deleted': 1}})
    return "OK"


@app.route("/delete/many/<name>", methods=['delete'])
def delete_many_by_name(name):
    db.delete_many({'name': name})
    return name


@app.route('/insert/student', methods=['post'])
def insert_student():
    data = request.get_data()
    data = str(data, encoding='utf-8')
    data = json.loads(data)
    stu = data['student']
    stu['deleted'] = 0
    print(stu)
    db.insert_one(stu)  # stu已经改变
    print(
        stu)  # 会自动添加一个ObjectId{'name': '小e', 'age': 30, 'hobby': ['running'], 'deleted': 0, '_id': ObjectId('5f1a9e8fe48b1b42a1c35e60')}
    return "OK"


# 高级查询

# 1、and 和 or查询 #默认 find 多个条件是隐式and
@app.route("/query")
def query_or():
    age = request.args.get("age")
    name = request.args.get("name")

    resp = db.find({'$or': [
        {'age': {'$gt': age}},  # 大于
        {'name': name}
    ]})

    return jsonify(list(resp))


# 2、嵌入式文档
# {
#    name ''
#    article:{
#       title: ''
#       tags:[aaaa]
#    }
# }
@app.route('/insert/user', methods=['post'])
def insert_user():
    data = request.get_data()
    data = str(data, encoding='utf-8')
    data = json.loads(data)
    user = data['user']
    print(user)
    db.insert_one(user)
    return "OK"


@app.route('/query/user')
def query_user():
    return jsonify(list(db.find({}, {'_id': 0})))


@app.route("/query/user/<title>")
def query_user_title(title):
    return jsonify(list(db.find(
        {
            'article.title': title
        },
        {'_id': 0, 'article.tags': 0}
    )))


# 3、数组查询
@app.route('/query/student/hobby/<hobby_name>')
def query_student_hobby(hobby_name):
    return jsonify(list(db.find(
        {'$or': [
            {'hobby': hobby_name},
            {'hobby': 'running'}
        ]},  # 查询数组 hobby含有 hobby_name的 可以多个 and关系 or关系  'hobby':['basketball','football']
        {'_id': 0}
    )))


#按数组长度查询
@app.route('/query/hobby/size/<int:size>')
def query_hobby_size(size):
    return jsonify(list(db.find(
        {'hobby':{'$size':size}},
        {'_id':0}
    )))

#根据条件查询
# {'name':'','price':[1,2,3,4]}
# db.find({'price':{'$lt':300,'$gt':100}})


#根据索引查询
#db.find({'price.0':{'$gt':100} })
#db.find({'price.1':'100'})



if __name__ == '__main__':
    app.run(port=8080, debug=True)
