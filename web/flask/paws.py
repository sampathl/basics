from flask import Flask,render_template

app = Flask(__name__)


"""Information regarding the Pets in the System."""
Pets = [
            {"id": 1, "name": "Nelly", "age": "5 weeks", "bio": "I am a tiny kitten rescued by the good people at Paws Rescue Center. I love squeaky toys and cuddles."},
            {"id": 2, "name": "Yuki", "age": "8 months", "bio": "I am a handsome gentle-cat. I like to dress up in bow ties."},
            {"id": 3, "name": "Basker", "age": "1 year", "bio": "I love barking. But, I love my friends more."},
            {"id": 4, "name": "Mr. Furrkins", "age": "5 years", "bio": "Probably napping."}, 
        ]


@app.route("/home")
def home():
    return render_template("home_paws.html", pets=Pets)

@app.route("/about")
def about():
    return render_template("about_paws.html")

@app.route("/details/<int:id>")
def details(id):
    
    return render_template("details_paws.html", pet=Pets[id-1])


if __name__ == "__main__":
    app.run()