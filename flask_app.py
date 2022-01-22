
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("ui1/index.html")

@app.route('/uid2')
def uid2():
    return render_template("ui2/index.html")

@app.route('/uid3')
def uid3():
    return render_template("ui3/index.html")

@app.route('/uid4')
def uid4():
    return render_template("ui4/index.html")

@app.route('/uid5')
def uid5():
    return render_template("ui5/index.html")

@app.route('/uid6')
def uid6():
    return render_template("ui6/index.html")


@app.route('/uid7')
def uid7():
    return render_template("ui7/index.html")

@app.route('/uid8')
def uid8():
    return render_template("ui8/index.html")

@app.route('/uid9')
def uid9():
    return render_template("ui9/index.html")

@app.route('/uid10')
def uid10():
    return render_template("ui10/index.html")

@app.route('/uid11')
def uid11():
    return render_template("ui11/index.html")


@app.route('/uid12')
def uid12():
    return render_template("ui12/index.html")
