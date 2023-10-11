from flask import Flask, render_template, url_for, request, redirect
import basededonnees 
#from flask_jsglue import JSGlue
#from markupsafe import Markup

app = Flask(__name__)
#JSGlue(app)

##################################################### ADMINISTRATEUR #####################################
##################################################### connexion admin ####################################
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method=='POST':
        username = request.form.get("username")
        password = request.form.get("password")

        # Vérifiez le nom d'utilisateur et le mot de passe dans la base de données

        if basededonnees.usernameadmin_exists(username) and basededonnees.passwordadmin_is_correct(username, password):
            # Le nom d'utilisateur et le mot de passe sont corrects
            return redirect(url_for('adminindex'))
        else:
            # Le nom d'utilisateur et le mot de passe sont incorrects
            return render_template("adminregister.html", error="Le nom d'utilisateur ou le mot de passe est incorrect")
    return render_template("admin.html")

################################################## register admin ###########################################
@app.route('/adminregister', methods=['GET', 'POST'])
def adminregister():
    if request.method=='POST':
            username = request.form.get("username")
            password = request.form.get("password")
            basededonnees.ajouter_admin(username, password)
            return redirect(url_for('admin'))
    return render_template('adminregister.html')
############################################## Tableau de bord ##############################################
@app.route('/adminindex')
def adminindex():
     return render_template("adminindex.html")
@app.route('/ajouterusers')
def ajouterusers():
     return render_template("ajouterusers.html")
@app.route('/afficherusers')
def afficherusers():
     return render_template("afficherusers.html")
@app.route('/afficherlivre')
def afficherlivre():
     return render_template("afficherlivre.html")
#################################################### FIN ADMINISTRATEUR #######################################
#################################################### UTILISATEUR ##############################################
#################################################### CONNEXION UTILISATEUR ####################################
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        username = request.form.get("username")
        password = request.form.get("password")

        # Vérifiez le nom d'utilisateur et le mot de passe dans la base de données

        if basededonnees.username_exists(username) and basededonnees.password_is_correct(username, password):
            # Le nom d'utilisateur et le mot de passe sont corrects
            return redirect(url_for('index'))
        else:
            # Le nom d'utilisateur et le mot de passe sont incorrects
            return render_template("register.html", error="Le nom d'utilisateur ou le mot de passe est incorrect")
    return render_template("login.html")
#################################################### ENREGISTREMENT UTILISATEUR ##############################
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
############################################### ACCEUIL UTILISATEUR ###########################################
@app.route('/index')
def index():
    return render_template("index.html")
############################################# APROPOS UTILISATEUR ##############################################
@app.route('/about', methods=['GET', 'POST'])
def about():
     return render_template("about.html")
############################################# OUVRAGE UTILISATEUR ##############################################
@app.route('/product')
def product():
     return render_template("product.html")
############################################# CONTACT UTILISATEUR ##############################################
@app.route('/contact')
def contact():
     return render_template("contact.html")





if __name__=='__main__':
    app.run(debug=True)