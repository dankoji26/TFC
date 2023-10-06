import mysql.connector
import pymysql
import time
'''from flask_jsglue import JSGlue'''



def afficher_users():
    conn = mysql.connector.connect(user='root', password='',
                                host='localhost',
                                database='librairie')
    cursor = conn.cursor()
    cursor.execute(""" SELECT * FROM users """)
    rows = cursor.fetchall()
    return rows
    conn.commit()
    conn.close()

def ajouter_users(username, email, password, nom, postnom, date_naisse, categorie, genre):
     conn = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='librairie')

     reference = (username, email, password, nom, postnom, date_naisse, categorie, genre)
     cursor = conn.cursor()
     cursor.execute(""" INSERT INTO users(username, email, password, nom, postnom, date_naisse, categorie, genre) VALUES(%s,%s,%s, %s,%s,%s, %s,%s)""", reference)
     conn.commit()
     conn.close()

def supprimer_users():
     conn = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='librairie')
     cursor = conn.cursor()
     cursor.execute(""" DELETE FROM users WHERE id==%s """)
     rows = cursor.fetchall()
     return rows
     conn.commit()
     conn.close()

def afficher_ouvrage():
    conn = mysql.connector.connect(user='root', password='',
                                host='localhost',
                                database='librairie')
    cursor = conn.cursor()
    cursor.execute(""" SELECT image, name, author, price, devise, category FROM ouvrage """)
    rows = cursor.fetchall()
    return rows
    conn.commit()
    conn.close()

def ajouter_ouvrages(date, img, nom, prix, auteur, categorie):
     conn = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='librairie')

     reference = (date, img, nom, prix, auteur, categorie)
     cursor = conn.cursor()

     cursor.execute(""" INSERT INTO ouvrage(image, name, author, price, devise, category) VALUES(%s,%s,%s,%f,%s,%s)""", reference)
     conn.commit()
     conn.close()

def supprimer_ouvrage():
     conn = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='librairie')
     cursor = conn.cursor()
     cursor.execute(""" DELETE FROM ouvrage WHERE id==%s """)
     rows = cursor.fetchall()
     return rows
     conn.commit()
     conn.close()
'''def technicien():
    conn = mysql.connector.connect(user='root', password='',
                                host='localhost',
                                database='donnees')
    cursor = conn.cursor()
    cursor.execute(""" SELECT * FROM technicien """)
    rows = cursor.fetchall()
    return rows
    conn.commit()
    conn.close()

def temps():
    conn = mysql.connector.connect(user='root', password='',
                                host='localhost',
                                database='donnees')
    cursor = conn.cursor()
    cursor.execute(""" SELECT * FROM temps """)
    rows = cursor.fetchall()
    return rows
    conn.commit()
    conn.close()'''


     

     


'''def infos_site():
    conn = mysql.connector.connect(user='root', password='',
                                host='localhost',
                                database='donnees')
    cursor = conn.cursor()
    cursor.execute(""" SELECT idPanne, panne, nomSite, Equipement, Adresse, Categorie, date, heure, alarme, etat, Intervenant FROM \
        configuration INNER JOIN  panne""")
    rows = cursor.fetchall()
    return rows
    conn.commit()
    conn.close()'''

'''def mise_jour(button, nomsite, id):
    conn = mysql.connector.connect(user='root', password='',
                                host='127.0.0.1',
                                database='donnees')
    heure = str(time.strftime("%H:%M:%S"))
    reference = (button, id)
    reference2 = (id, nomsite, button, heure)
    cursor = conn.cursor()
    valeur = cursor.execute("")
    cursor.execute(""" UPDATE panne SET Etat=%s WHERE idPanne=%s """, reference)
    cursor.execute(""" INSERT INTO temps(num,nomSite,etat ,heure) VALUES(%s, %s, %s, %s) """, reference2)
    conn.commit()
    conn.close()'''
########################################################################################
# LES VERIFICATION POUR LE NOM D'UTILISATEUR ET LE MOT DE PASSE DANS LA BASE DE DONNEES#
########################################################################################
def username_exists(username):
    # Connectez-vous à la base de données
    conn = pymysql.connect(host="localhost", user="root", password="", database="librairie")

    # Créez un curseur
    cur = conn.cursor()

    # Exécutez la requête SQL pour vérifier si le nom d'utilisateur existe
    sql = "SELECT COUNT(*) FROM users WHERE username = '{}'".format(username)
    cur.execute(sql)

    # Récupérez le nombre de résultats
    count = cur.fetchone()[0]

    # Fermez le curseur et la connexion à la base de données
    cur.close()
    conn.close()

    # Renvoyez True si le nom d'utilisateur existe, False sinon
    return count > 0

def password_is_correct(username, password):
    # Connectez-vous à la base de données
    conn = pymysql.connect(host="localhost", user="root", password="", database="librairie")

    # Créez un curseur
    cur = conn.cursor()

    # Exécutez la requête SQL pour récupérer le mot de passe du nom d'utilisateur donné
    sql = "SELECT password FROM users WHERE username = '{}'".format(username)
    cur.execute(sql)

    # Récupérez le mot de passe
    password_hash = cur.fetchone()[0]

    # Fermez le curseur et la connexion à la base de données
    cur.close()
    conn.close()

    # Vérifiez si le mot de passe donné correspond au mot de passe hashé dans la base de données
    return password == password_hash

#aff= afficher_ouvrage()
#print(aff)