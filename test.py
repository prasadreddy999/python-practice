from flask import Flask
from flask import render_template
app = Flask(__name__)

### this is from sql direcory
@app.route("/")
def hello():
    return "Prasad"

@app.route("/prasad")
def prasad():
    return "Welcome to Prasad"

@app.route("/prasadd")
def sindhu():
    return render_template('test2.html')

if __name__ == "__main__":
    app.run()
