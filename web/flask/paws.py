from flask import Flask,render_template
from flask import request
from form import LoginForm

app = Flask(__name__)


"""Information regarding the Pets in the System."""
Pets = [
            {"id": 1, "name": "Nelly", "age": "5 weeks", "bio": "I am a tiny kitten rescued by the good people at Paws Rescue Center. I love squeaky toys and cuddles."},
            {"id": 2, "name": "Yuki", "age": "8 months", "bio": "I am a handsome gentle-cat. I like to dress up in bow ties."},
            {"id": 3, "name": "Basker", "age": "1 year", "bio": "I love barking. But, I love my friends more."},
            {"id": 4, "name": "Mr. Furrkins", "age": "5 years", "bio": "Probably napping."}, 
        ]

app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf' 
users = {
    "archie.andrews@email.com": "football4life",
    "veronica.lodge@email.com": "fashiondiva"
}

@app.route("/home")
def home():
    return render_template("home_paws.html", pets=Pets)

@app.route("/about")
def about():
    return render_template("about_paws.html")

@app.route("/details/<int:id>")
def details(id):
    
    return render_template("details_paws.html", pet=Pets[id-1])

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":
        print("long in submitted")  
        return render_template("login.html", id=request.form.get("email"))
    form = LoginForm()  
    return render_template("login.html", form = form)

if __name__ == "__main__":
    app.run()