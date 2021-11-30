from flask import Flask, render_template   #from flask package we have imported Flask class

app = Flask(__name__)   #Flask class object and gives a name which is unique

@app.route("/firstpage")
def hello_world():
    return render_template(
        "jinja_intro.html",name = "Anuj Kaushik", template_name = "Jinja 2"
        
        )



