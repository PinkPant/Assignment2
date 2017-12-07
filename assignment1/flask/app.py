from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask: Hello World\n'

if __name__ == '__main__':
    app.run(debug=false,host='0.0.0.0',port=8080)

