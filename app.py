from flask import Flask, render_template   #from flask package we have imported Flask class

app = Flask(__name__)   #Flask class object and gives a name which is unique


@app.route("/conditional-basics/")
def render_data_structures():
    
    company = "Apple"

    return render_template("conditional_basics.html", company = company)

    
 


