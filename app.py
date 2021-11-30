from flask import Flask, render_template   #from flask package we have imported Flask class

app = Flask(__name__)   #Flask class object and gives a name which is unique

class GalileanMoons:
    def __init__(self, first, second, third, fourth):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth

@app.route("/data-structures/")
def render_data_structures():

    movies = [
        "Leon the professional",
        "The usual Suspects",
        "A beautiful mind"
    ]

    car = {
        "brand" : "Tesla",
        "model" : "Roadster",
        "Year" : "2020"
    }

    moons = GalileanMoons("IO", "Europa", "Ganime", "Calisto")

    kwargs = {
        "movies" : movies,
        "car" : car,
        "moons" : moons
    }


    return render_template("data_structures.html", **kwargs)

    
 


