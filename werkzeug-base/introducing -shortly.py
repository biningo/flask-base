from werkzeug import Response, Request, run_simple


class Shortly():
    def __init__(self,server_name):
        self.server_name = server_name

    def dispath_request(self,request):
        print(request.path,request.method)
        name = request.args.get("name") if request.args.get("name") else "undefined"
        return Response("hello,"+name)

    def wsgi_app(self,environ,start_response):
        request = Request(environ)
        response = self.dispath_request(request)
        return response(environ,start_response)
    def __call__(self, environ,start_response):
        return self.wsgi_app(environ,start_response)

def create_app(server_name='There is no'):
    app = Shortly(server_name)

    return app


if __name__ == '__main__':
    app = create_app("ubuntu")
    run_simple('localhost',8080,application=app,use_debugger=True,use_reloader=True)