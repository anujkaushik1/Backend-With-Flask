from flask import Flask, render_template   #from flask package we have imported Flask class

app = Flask(__name__)   #Flask class object and gives a name which is unique

@app.route("/firstpage")
def hello_world():
    return render_template("first_page.html")

@app.route("/secondpage")
def hello_world_fancy():
    return render_template("second_page.html")


