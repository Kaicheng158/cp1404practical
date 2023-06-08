from flask import Flask

app = Flask(__name__)


# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'

# @app.route('/greet')
# @app.route('/greet/<name>')
# def greet(name=""):
#     return f"Hello {name}"

@app.route('/f/<celsius>')
def f(celsius=""):
    celsius = float(celsius)
    fahrenheit = 32 + celsius * 1.8
    return f"{fahrenheit}"


if __name__ == '__main__':
    app.run()