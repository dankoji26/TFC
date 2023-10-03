import mysql.connector
import time



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
                              database='libraire')

     reference = (username, email, password, nom, postnom, password, date_naisse, categorie, genre)
     cursor = conn.cursor()
     cursor.execute(""" INSERT INTO users(username, email, password, nom, postnom, password, date_naisse, categorie, genre) VALUES(%s,%s,%s, %s,%s,%s, %s,%s,%s)""", reference)
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

aff= afficher_ouvrage()
print(aff)