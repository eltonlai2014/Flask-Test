from flask import Flask,request,Response,jsonify

from db.query import test
import os
app = Flask(__name__)
app.secret_key = "123456"

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

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
    print(os.environ.keys())