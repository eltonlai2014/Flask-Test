from flask import Flask

app = Flask(__name__)
app.secret_key = "123456"

@app.route("/")
def index():
    return "hello world"

"""
Flask 路由
"""
@app.route("/hello/name/<name>")
def hello_name(name):
    return "hello %s" %name




if __name__ == "__main__":
    app.run(debug=True)