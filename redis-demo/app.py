import json

from flask import Flask, jsonify, request
import redis
app = Flask(__name__)

Client = redis.Redis(host='118.178.180.115',db=2,password='biningo')


# ---------------key val------------------
@app.route('/get/keys')
def get_keys():
    keys = Client.keys()
    keys = map(lambda x:str(x,encoding='utf-8'),keys)
    return jsonify(list(keys))

@app.route('/set/key',methods=['post'])
def set_key():
    data = request.get_data()
    data = json.loads(data)
    print(data)
    key = data['key']
    val = data['val']
    resp = Client.set(key,val) #False True
    return "OK" if resp else "No"

@app.route('/get/<key>')
def get_key(key):
    val = Client.get(key)
    return str(val,encoding='utf-8') if val else "None"

@app.route('/delete/<key>',methods=['delete'])
def delete_key(key=''):
    resp = Client.delete(key)
    return "OK" if resp else "No"

# --------------------计数器--------------
@app.route('/incr/count')
def incr_count():
    resp = Client.incr('count') #不存在的话先执行 set count 0 然后+1
    return str(resp)
@app.route('/decr/count')
def decr_count():
    resp = Client.decr('count') #不存在的话 先执行 set count 0  然后-1
    return str(resp)
# ------------------------------------------



#------------------list--------------------
@app.route('/list/lpush',methods=['post'])
def list_lpush():
    data = json.loads(request.get_data())
    key = data['key']
    val = data['val']
    resp = Client.lpush(key,val) #返回push成功的值
    print(resp)
    return "OK" if resp else "No"

@app.route('/list/rpush',methods=['post'])
def list_rpush():
    data = json.loads(request.get_data())
    key = data['key']
    val = data['val']
    resp = Client.rpush(key, val) #返回push成功的值
    return "OK" if resp else "No"

@app.route('/list/lpop/<key>')
def list_lpop(key):
    val = Client.lpop(key)
    return str(val,encoding='utf-8') if val else "None"


@app.route('/list/rpop/<key>')
def list_rpop(key):
    val = Client.rpop(key)
    print(val) #byte
    return str(val,encoding='utf-8') if val else "None"


@app.route('/list/len/<key>')
def list_len(key):
    resp = Client.exists(key) #返回0、1
    if not resp:
        return 'None'
    len = Client.llen(key)
    return str(len)

@app.route('/list/range/<key>')
def list_lrange(key):
    left = request.args.get('left')
    left = left if left else 0
    right = request.args.get('right')
    right = right if right else -1
    resp = Client.lrange(key,start=left,end=right)
    resp = list(map(lambda x:str(x,encoding='utf-8'),resp))
    return jsonify(resp)








if __name__ == '__main__':
    app.run(port=8080,debug=True)




