# https://www.xncoding.com/2016/12/02/python/werkzeug.html
from werkzeug import Request, Response

# werkzeug wrap request and response
from werkzeug.serving import make_server


def application(environ,start_response):
    request = Request(environ)
    content = "hello,"+request.args.get("name","defaultName")
    response = Response(content,mimetype="text/plain")
    return response(environ,start_response)

if __name__ == '__main__':
    server = make_server("localhost",8080,application)
    server.serve_forever()
