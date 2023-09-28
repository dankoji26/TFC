import mysql.connector
import time



def afficher():
    conn = mysql.connector.connect(user='root', password='',
                                host='localhost',
                                database='librairie')
    cursor = conn.cursor()
    cursor.execute(""" SELECT * FROM users """)
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

def ajouter_users(username, email, password, nom, postnom, date_naisse, categorie, genre):
     conn = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='libraire')

     reference = (username, email, password, nom, postnom, password, date_naisse, categorie, genre)
     cursor = conn.cursor()
     cursor.execute(""" INSERT INTO users(username, email, password, nom, postnom, password, date_naisse, categorie, genre) VALUES(%s,%s,%s, %s,%s,%s, %s,%s,%s)""", reference)
     conn.commit()
     conn.close()
     
'''def ajouter_technicien(nom, postnom, password, fonction, numtel):
     conn = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='donnees')

     reference = (nom, postnom, password, fonction, numtel)
     cursor = conn.cursor()

     cursor.execute(""" INSERT INTO technicien(nom,post_nom,password,fonction,numtel) VALUES(%s,%s,%s,%s,%s)""", reference)
     conn.commit()
     conn.close()'''
     
def afficher_ouvrage():
     conn = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='libraire')
     cursor = conn.cursor()
     cursor.execute(" SELECT date, img, nom, prix, description, auteur, categorie")
     rows = cursor.fetchall()
     return rows

     conn.commit()
     conn.close()


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

aff= afficher()
print(aff)