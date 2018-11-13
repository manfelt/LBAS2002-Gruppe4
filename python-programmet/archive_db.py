import pymysql
from tkinter import messagebox
import sys

"""
Skrevet av: Majid Rouhani
Opprettet: 11.09.2018
Versjon: 1.0

Beskrivesle:
Denne modulen leser data fra databasen eller registrerer/oppdaterer gjenstander.
NB! Oppdater variablene user/password slik at de inneholder rett database tilgang.
-----------------------------------------------------------------------------------------------------------
Endret dato, endret av, versjon
<02.11.2018>, <Berit Gudmundseth>, <1.1> 4.1 Registrere ny gjenstand og kategori. 
<03.11.2018>, <Maria Seljeseth>, <1.2> 4.2 Søk
<03.11.2018>, <Simen Myhre>, <1.3> 4.3 Slette gjenstand. 
-----------------------------------------------------------------------------------------------------------
"""

host = "mysql.stud.iie.ntnu.no"
user = "beritgud" # Skriv inn brukernavnet ditt her
password = "L1Hh7Pgd" # Skriv inn passordet ditt her

def get_db_connection():
    if user=="":
        messagebox.showerror("Error", "User/password for database kobling er ikke satt. Sjekk filen archive_db")
        return False
    else:
        return pymysql.connect(host, user, password, user)

# Søk på gjenstander, gitt navn og/eller registreringsnummer
def search(name, regnr):
    """
    :param name: navn på gjenstand. Denne kan være tom, dvs "" eller være hele/deler av navnet. Case-sensitive!
    :param regnr: registreringsnummer på gjenstand. Denne kan være tom, dvs "" eller være hele/deler av registreringsnummeret. Case-sensitive!
    :return: returnerer en 2-dimensjonal liste med søkeresultater
    """
    db = get_db_connection()

    if not db:
        sys.exit(0)

    cursor = db.cursor()
    
    # Logger inputdata til konsollet
    print("search: name=" + name + ", regnr=" + regnr)

    cursor.execute("SELECT regnr,navn,regdato,regav FROM gjenstand WHERE navn LIKE %s AND regnr LIKE %s", ("%"+name+"%", "%"+regnr+"%"))
    
    result = []
    for row in cursor:
        gjenstand = []
        gjenstand.append(row[0]) #regnr
        gjenstand.append(row[1]) #navn
        gjenstand.append(row[2]) #regdato
        gjenstand.append(row[3]) #regav
       
        result.append(gjenstand)

    db.close()
    
    # Logger antall rader funnet til konsollet
    print("search: rowcount=" + str(len(result)))
    
    return result

#Slett gjenstand
def delete_gjenstand(registreringsnr):

    db = get_db_connection()
    db.autocommit(True)
    
    cursor = db.cursor()
    cursor.execute("DELETE FROM egenskaper WHERE regnr=%s", (registreringsnr))
    cursor.execute("DELETE FROM proveniens WHERE regnr=%s", (registreringsnr))
    cursor.execute("DELETE FROM kategori WHERE kategori_id=%s", (registreringsnr))
    cursor.execute("DELETE FROM gjenstand WHERE regnr=%s", (registreringsnr))
    
    db.close()
                   
    print("delete_gjenstand: "+registreringsnr)


# Hent alle materialet og antall av hver som to lister
def get_materialet_counts():
    """
    Les antall gjenstander fra databasen gruppert på 'materialet'
    Legg resultatet i to lister: materialet og counts
    :return: counts (liste med tall), materialet (liste med gjenstands materialet)
    """
    db = get_db_connection()

    if not db:
        sys.exit(0)

    cursor = db.cursor()
    cursor.execute("SELECT count(regnr),materiale FROM egenskaper group by materiale")

    materiale = []
    counts = []
    for row in cursor:
        materiale.append(row[0])
        counts.append(row[1])

    db.close()

    # Logger antall rader funnet til konsollet
    print("get_materialet_counts: rowcount=" + str(len(materiale)))

    return counts, materiale

# Hent all informasjon om en gjenstand basert på regnr
def hent_gjenstand(regnr):
    """
    Henter all informasjon om en gjebstand for en gitt registreringsnr
    :param regnr: Regnr er av typen string
    :return: Returnerer resultatet i en 2-dimensjonal tabell.
             Tabellen vil alltid inneholde en gjenstand da vi søker etter eksakt treff og regnr er primær-nøkkel
    """
    db = get_db_connection()

    if not db:
        sys.exit(0)

    cursor = db.cursor()

    cursor.execute("""
            SELECT giver,inndato,kommentar,mottattav,navn,plassering,regav,regdato,g.regnr,katnavn,fys_egenskap,maal,materiale,tilstand,produsent,prod_aar,siste_eier,tidl_eiere 
              FROM gjenstand g, 
                   egenskaper e, 
                   kategori k, 
                   proveniens p 
            WHERE g.regnr = e.regnr 
              AND g.kategori_id = k.kategori_id 
              AND g.regnr = p.regnr
              AND g.regnr = %s """, regnr)

    result = []
    for row in cursor:
        print(row)
        gjenstand = []
        for r in range(len(row)):
            gjenstand.append(row[r])
        result.append(gjenstand)

    db.close()

    # Logger antall rader funnet til konsollet
    print("search: rowcount=" + str(len(result)))

    return result

#Get next kategori_id
def get_next_category_id():
    """
    Finn neste kategori_id for registrering av ny gjenstand.
    :return: hente siste kategori_id fra basen og øk tallet med 1. Returner dette
    """
    db = get_db_connection()

    if not db:
        sys.exit(0)

    cursor = db.cursor()
    cursor.execute("SELECT max(kategori_id) as kategori_id FROM kategori")

    kategoti_id = ""

    for row in cursor:
      kategoti_id=  str(row[0])

    db.close()

    # Logger antall rader funnet til konsollet
    print("kategoti_id: " + kategoti_id)

    if int(kategoti_id)==0:
        next_kategoti_id=1
    else:
        next_kategoti_id = int(kategoti_id)+1

    return next_kategoti_id

#Sjekk om regnr existerer i databasen
def regnr_exist(regnr,tabellnavn):
    """
    Sjekk om regnnr existerer allerede i basen
    :param regnr: type string
    :return: boolean
    """
    db = get_db_connection()

    if not db:
        sys.exit(0)

    cursor = db.cursor()
    sql = "SELECT count(regnr) as regnr_count FROM {0} WHERE regnr='{1}'".format(tabellnavn,regnr)
    cursor.execute(sql)

    regnr_count = 0

    for row in cursor:
      regnr_count=  row[0]

    db.close()

    # Logger antall rader funnet til konsollet
    print("regnr_count: " + str(regnr_count))

    if regnr_count==0:
        return False
    else:
        return True

#Sjekk om kategori_id existerer i basen
def kategori_exist(kategori_id):
    """
    Sjekk om kategori_id existerer i databasen
    :param kategori_id: int
    :return: boolean
    """
    db = get_db_connection()

    if not db:
        sys.exit(0)

    cursor = db.cursor()
    cursor.execute("SELECT count(kategori_id) as kategori_id_count FROM kategori WHERE kategori_id=%s",kategori_id)

    kategori_id_count = 0

    for row in cursor:
      kategori_id_count=  row[0]

    db.close()

    # Logger antall rader funnet til konsollet
    print("kategori_id_count: " + str(kategori_id_count))

    if kategori_id_count==0:
        return False
    else:
        return True

#Lagre kategori info i basen
def save_cateogri_db(kategori_id, kategori):
   
    db = get_db_connection()
   
    if not db:
        sys.exit(0)
    
    db.autocommit(True)
    cursor = db.cursor()
    
    if kategori_exist(kategori_id):
        cursor.execute("UPDATE kategori SET katnavn=%s WHERE kategori_id=%s", kategori_id, kategori)
    else:
        cursor.execute("INSERT INTO kategori (kategori_id,katnavn) VALUES(%s,%s)",
                   (kategori_id, kategori))
    db.close()
   
    print("save_cateogri_db: rowcount=" + str(cursor.rowcount))

#Lagrer gjenstand i basen
def save_gjenstand_db(giver_val,
                      innlemmet_dato_val,
                      kategori_id,
                      kommentar_val,
                      mottatt_av_val,
                      navn_val,
                      plassering_val,
                      registrert_av_val,
                      registrerings_dato_val,
                      regnr):

    db = get_db_connection()
    
    if not db:
        sys.exit(0)
    
    db.autocommit(True)
    cursor = db.cursor()
    
    if regnr_exist(regnr, 'gjenstand'):
            cursor.execute("UPDATE gjenstand SET giver=%s, inndato=%s, kategori_id=%s, kommentar=%s, mottattav=%s, navn=%s, plassering=%s, regav=%s, regdato=%s WHERE regnr=%s",
                           (giver_val, innlemmet_dato_val, kategori_id, kommentar_val, mottatt_av_val, navn_val, plassering_val, registrert_av_val, registrerings_dato_val, regnr))
    else:
            cursor.execute("INSERT INTO gjenstand (giver, inndato, kategori_id, kommentar, mottattav, navn, plassering, regav, regdato, regnr) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                           (giver_val, innlemmet_dato_val, kategori_id, kommentar_val, mottatt_av_val, navn_val, plassering_val, registrert_av_val, registrerings_dato_val, regnr))
    
    db.close()

    print("save_gjenstand_db: rowcount=" + str(cursor.rowcount))

#Lagre egenskaper til gjenstand
def save_egenskaper_db(fysiske_egenskaper_val,
                       maal_val,
                       materiale_val,
                       regnr,
                       tilstand_val):
    """
    Lagre egenskaper til gjenstand i 'egenskper' tabellen
    :param fysiske_egenskaper_val: string
    :param maal_val: string
    :param materiale_val: string
    :param regnr: string
    :param tilstand_val: string
    :return:
    """
    db = get_db_connection()

    if not db:
        sys.exit(0)

    db.autocommit(True)
    cursor = db.cursor()

    if regnr_exist(regnr,'egenskaper'):
        cursor.execute("UPDATE egenskaper SET fys_egenskap=%s,maal=%s,materiale=%s,tilstand=%s WHERE regnr=%s",
                   (fysiske_egenskaper_val,maal_val,materiale_val,tilstand_val,regnr))
    else:
        cursor.execute("INSERT INTO egenskaper (fys_egenskap,maal,materiale,regnr,tilstand) VALUES(%s,%s,%s,%s,%s)",
                   (fysiske_egenskaper_val,maal_val,materiale_val,regnr,tilstand_val))

    db.close()

    # Logger resultatet til konsollet
    print("save_egenskaper_db: rowcount=" + str(cursor.rowcount))

#Lagre proveniens til 'proveniens' tabellen
def save_proveniens_db(produsent_val,produksjonsaar_val,regnr,giver_siste_eier_val,tidligere_eiere_val):
    """
    Lagre proveniens i 'proveniens' tabellen i databasen
    :param produsent_val: string
    :param produksjonsaar_val: string
    :param regnr: string
    :param giver_siste_eier_val: string
    :param tidligere_eiere_val: string
    :return:
    """
    db = get_db_connection()

    if not db:
        sys.exit(0)

    db.autocommit(True)
    cursor = db.cursor()

    if regnr_exist(regnr,'proveniens'):
        cursor.execute("UPDATE proveniens SET produsent=%s,prod_aar=%s,siste_eier=%s,tidl_eiere=%s WHERE regnr=%s",
                   (produsent_val,produksjonsaar_val,giver_siste_eier_val,tidligere_eiere_val,regnr))
    else:
        cursor.execute("INSERT INTO proveniens (produsent,prod_aar,regnr,siste_eier,tidl_eiere) VALUES(%s,%s,%s,%s,%s)",
                   (produsent_val,produksjonsaar_val,regnr,giver_siste_eier_val,tidligere_eiere_val))

    db.close()

    # Logger resultatet til konsollet
    print("save_proveniens_db: rowcount=" + str(cursor.rowcount))

