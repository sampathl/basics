from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hellow():
    return "hellow world"

@app.route("/static")
def sam():
    return "this is a test for static"

@app.route("/square/<int:number>")
def square(number:int):
    return "The provided number is {number} and it's square is {square}".format(number=number,square=number**2)

@app.route("/home")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)

