import logging

from flask import Flask, request

app = Flask(__name__)

# logging flask使用内置的的logging模块

@app.route("/")
def log():
    app.logger.info(request.method)
    app.logger.error("error")
    app.logger.warning("warn")
    return "Ok"

if __name__ == '__main__':
    app.run(port=8080,debug=True)