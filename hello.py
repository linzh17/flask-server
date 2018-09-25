from flask import Flask 
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>nihao</h1>'

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=50001,debug=True)
