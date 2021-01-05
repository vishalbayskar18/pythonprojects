from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    print ("Welcome to my universe ...")
    return "Hello World!"

@app.route('/hi')
def hi():
    return "Hi How Are you"
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)



