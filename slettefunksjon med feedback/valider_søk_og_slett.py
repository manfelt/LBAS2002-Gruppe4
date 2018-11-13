import pymysql


def valider_pers_id(pers_id):
    har_resultat = False
    db = pymysql.connect("mysql.stud.iie.ntnu.no","simenmyh","bcyFp79h","simenmyh") # Brukernavn, Passord og databaseavn
    cursor = db.cursor()
    finn_pers_id = cursor.execute("SELECT * from person where pers_id=%s", (pers_id))
    for finn_pers_id in cursor:
        har_resultat = True
        print("person id:", pers_id, "funnet")
    if not har_resultat:
        print("person id:", pers_id, "ikke funnet")
    db.close()

def valider_slettet_person(pers_id):
    har_resultat = False
    db = pymysql.connect("mysql.stud.iie.ntnu.no","simenmyh","bcyFp79h","simenmyh") # Brukernavn, Passord og databaseavn
    cursor = db.cursor()
    finn_pers_id = cursor.execute("SELECT * from person where pers_id=%s", (pers_id))
    for finn_pers_id in cursor:
        har_resultat = True
        print("person id:", pers_id, "ble ikke slettet eller eksisterer")
    if not har_resultat:
        print("person id:", pers_id, "ble slettet eller eksisterer ikke")
    db.close()

