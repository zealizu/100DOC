from flask import Flask


app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper
@app.route("/")
def hello_world():
    return "<p>Hello, sir!</p>"\
        "<p>hi there</p>"

@app.route("/bye")
@make_bold
def bye():
    return "BYE"

@app.route("/username/<name>")
def greet(name):
    return f"Hello there {name}"
    
@app.route("/<number>")
def guess(number):
    return f"let me guess {number}"

if __name__ == "__main__":
    #Rn app in debug mode to auto reload
    app.run(debug=True)