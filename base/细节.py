from flask import Flask
app = Flask(__name__)

#1、--------------加斜杠和不加都是可以的---------------
@app.route('/ping1') # 访问/ping1/    无法访问
def ping1():
    return "ping1"

@app.route('/ping2/') #访问 /ping2 会重定向为 /ping2/
def ping2():
    return 'ping2'



#2、-----------------------





if __name__ == '__main__':
    app.run(port=8080)