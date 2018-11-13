import person_db
import pymysql
import valider_søk_og_slett


"""person_db.opprett_person("Bjørnstjerne Børspn", "Norge")
person_db.endre_navn("Bjørnstjerne Bjørnson", "Norge")
print(person_db.finn_personer("Norge"))
person_db.slett_person("Bjørnstjerne Bjørnson")"""
#Erstatt brukernavn, passord og database med din egen. putt test_db_sql.txt inn i SQL for å teste dette programmet
#person_db.py er ikke nødvendig for programmet, men ka være nyttig til testing av det. (men det er ikke helt oppdatert til databasens nye format.
#Erstatt pers_id med regnr hvis det skal testes med løsningsforslaget


#Erstatt delete_person med delete_gjenstand
def delete_person(pers_id):
    valider_søk_og_slett.valider_pers_id(pers_id)
    db = pymysql.connect("mysql.stud.iie.ntnu.no", "simenmyh","bcyFp79h","simenmyh")
    db.autocommit(True)
    cursor = db.cursor()
    sql1 = "DELETE FROM adresse WHERE pers_id=%s;"
    cursor.execute(sql1, pers_id)
    sql2 = "DELETE FROM yrke WHERE pers_id=%s;"
    cursor.execute(sql2, pers_id)
    sql3 = "DELETE FROM person WHERE pers_id=%s;"
    cursor.execute(sql3, pers_id)
    # Grunnen til at sql 1, 2 og 3 er delt opp er at hver "%s" refererer til per_id, men pers_id er bare ett argument, og kan ikke refereres til av alle tre. Jeg er usikker på hvordan jeg kan gjøre dette bedre.
    # Siden adresse tabellern og yrke tabellen har fremmednøkler som refererer til pers_id i person tabellen, er det viktig at de to slettes først, ellers vil ikke sql tillate at de blir slettet for å opprettholde integriteten i databasen.
    valider_søk_og_slett.valider_slettet_person(pers_id)
    db.close()
delete_person("2")

# Jeg tror programmet gjør det det er ment å gjøre, med unntak av tilbakemelding hvis noe går feil. Det kan helt sikker ryddes opp endel.
