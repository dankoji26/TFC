from flask import Flask, render_template, url_for, request, redirect
import basededonnees 
#from flask_jsglue import JSGlue
#from markupsafe import Markup

app = Flask(__name__)
#JSGlue(app)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        username = request.form.get("username")
        password = request.form.get("password")
        return redirect(url_for('index'))
    return render_template("login.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method=='POST':
            username = request.form.get("username")
            email = request.form.get("email")
            password = request.form.get("password")
            nom = request.form.get("nom")
            postnom = request.form.get("postnom")
            date_naisse = request.form.get("date_naisse")
            categorie = request.form.get("choix")
            genre = request.form.get("genre")
            basededonnees.ajouter_users(username, email, password, nom, postnom, date_naisse, categorie, genre)
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/index')
def index():
    return render_template("index.html")



if __name__=='__main__':
    app.run(debug=True)