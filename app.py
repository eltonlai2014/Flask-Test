from flask import Flask,request,Response,jsonify
from gevent.pywsgi import WSGIServer

from db.main import Test
from db.query import test
from test.file_test import ggg
import os

app = Flask(__name__)
app.secret_key = "123456"
ggg()

@app.route("/")
def index():
    model_list = test()

    print(model_list)
    data = jsonify({"data": {"supportModelList": model_list}})
    # return data, 200, {'Content-Type': 'application/json; charset=utf-8'}
    return data
    # return Response(data,mimetype='application/json')  #声明Content-Type为json格式
    # return "hello world"
"""
Flask 路由
"""
@app.route("/hello/name/<name>")
def hello_name(name):
    return "hello %s" %name

"""
if __name__ == "__main__":
    # Debug/Development
    app.run(debug=True, host="0.0.0.0", port="5000")
    # Production
    # http_server = WSGIServer(('', 5000), app)
    # http_server.serve_forever()
"""