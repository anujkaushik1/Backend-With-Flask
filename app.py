from flask import Flask, render_template   #from flask package we have imported Flask class

app = Flask(__name__)   #Flask class object and gives a name which is unique


@app.route("/for-loops/")
def render_loops_for():

    user_os = {
        "Bob Smith" : "Windows",
        "Anne Pun" : "MacOS",
        "Adam Lee" : "Linux",
        "Jose Salvatierra" : "Windows"

    }
    
    return render_template("for-loops.html", user_os = user_os)
 


