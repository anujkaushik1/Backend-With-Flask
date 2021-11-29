from flask import Flask   #from flask package we have imported Flask class

app = Flask(__name__)   #Flask class object and gives a name which is unique

@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/fancy")
def hello_world_fancy():
    return """
            <html>
            <body>

            <h1>Hello world</h1>
            <p> My name is anuj </p>
            

            </body>
            </html>
            """


