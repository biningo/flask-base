import json

from flask import Flask, jsonify, request
from pymongo import MongoClient



# collection.insert_many([
#     {'name': '小a', 'age': 10, 'hobby': ['basketball', 'running']},
#     {'name': '小b', 'age': 20, 'hobby': ['basketball', 'computer-games']}
# ])

class Student:
    def __init__(self,name='',age=None,hobby=[],email=''):
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
    students = list(db.find({'deleted':0},{'_id':0,'deleted':0}))
    return jsonify(students)

@app.route('/get/<stu_name>')
def get_by_name(stu_name):
    student = db.find_one({'name':stu_name,'deleted':0},{'_id':0,'deleted':0})
    return jsonify(student)

@app.route('/get/age')
def get_by_range_age():
    max_age = request.args.get('max_age')
    min_age = request.args.get('min_age')
    students = list(db.find({'age':{
        '$gt':int(min_age),
        '$lt':int(max_age)}},
        {'_id':0,'deleted':0}))
    return jsonify(students)

@app.route('/get/hobby')
def get_by_hobby():
    hobby_names = request.args.getlist('name')
    print(hobby_names)
    students = list(db.find({'hobby':{'$all':hobby_names}},{'_id':0,'deleted':0}))
    return jsonify(students)


@app.route('/get/max_age')
def get_max_age():
    students = db.find({},{'_id':0,'age':1}).sort('age').sort('name')
    res = students.limit(1)[0]
    print(list(students))
    return res

@app.route('/get/sort/age')
def get_sort_age():
    key = request.args.get("key")
    key  = int(key) if key else 1
    students = list(db.find({'deleted':0},{'_id':0,'deleted':0}).sort('age',key))
    return jsonify(students)




@app.route('/delete/<stu_name>',methods=['delete'])
def delete_by_name(stu_name):
    if db.find({'name':stu_name}).count()==0:
        return "No"
    db.update_one({'name':stu_name},{'$set':{'deleted':1}})
    return "OK"

@app.route("/delete/many/<name>",methods=['delete'])
def delete_many_by_name(name):
    db.delete_many({'name':name})
    return name

@app.route('/insert',methods=['post'])
def insert():
    data = request.get_data()
    data = str(data,encoding='utf-8')
    data = json.loads(data)
    stu = data['student']
    stu['deleted']=0
    print(stu)
    db.insert_one(stu) #stu已经改变
    print(stu) #会自动添加一个ObjectId{'name': '小e', 'age': 30, 'hobby': ['running'], 'deleted': 0, '_id': ObjectId('5f1a9e8fe48b1b42a1c35e60')}
    return "OK"





if __name__ == '__main__':
    app.run(port=8080,debug=True)
