from tkinter import *
import archive_edit
import archive_db
import archive_statistics
import matplotlib

"""
Programmet består av følgende moduler:
1) archive_main: Programmet startes ved å kjøre denne filen.
2) archive_db: Kommunikasjon mot databasen
3) archive_edit: Registrering/Redigering av data

For å kunne kjøre programmet, må du oppdatere archive_db modulen med påloggingsinformasjon (user/password).
-----------------------------------------------------------------------------------------------------------
Skrevet av:
<11.09.2018>, <Majid Rouhani>, <1.0>
Endret dato, endret av, versjon
<02.11.2018>, <Berit Gudmundseth>, <1.1> Endret noen navn.
<13.11.2018>, <Magnus Manfelt>, <1.2> Rettet på feil og mangler  
-----------------------------------------------------------------------------------------------------------
"""

# Global liste for søkeresultatet
result = []

# Definerer aksjon for arkivsøket
def search():
    """
    Søk i archive databasen
    Funksjonen kaller archive_edit.search metoden som returnerer en 2-dimensjonal liste med søkeresultater.
    (regnr,navn,regdato,regav)
    Fyller deretter listen "result_listbox" med resultatet.
    """
    result_listbox.delete(0, END)
    result.clear()
    db_result = archive_edit.search(name.get(), regnr.get())
    for element in db_result:
        result.append(element)
        result_listbox.insert(END, element[0]+", "+element[1]+", "+element[2]+", "+element[3])
       
# Definerer aksjon for menyvalget "Registrer Ny"
def new_archive():
    """"
    Kaller funksjonen archive_edit.open_edit som åpner et vindu for å registrere ny gjenstand
    """
    archive_edit.open_edit(root, search)

# Definerer aksjon for menyvalget "Vis aldersdistribusjon"
def view_materiale_statistics():
    """
     Kaller funksjonen archive_db.get_materialet_counts som returnerer liste med gjenstander grupper etter materialet og antall
     Deretter kalles funkasjonen archive_statistics.show_bar_chart for å tegne grafen.
    """
    counts, materiale = archive_db.get_materialet_counts()
    archive_statistics.show_bar_chart(materiale, counts, "Antall", "Materialet")


def view_kategori_statistics():
    counts, kategori = archive_db.get_kategori_counts()
    archive_statistics.show_bar_chart(kategori, counts, "Antall", "Kategori")



# Definerer aksjon for dobbeltklikk på en gjenstand i lista
def edit_gjenstand(event):
    """
    Når bruker dobbel-klikker på en gjenstand i listen (søke-resultatet), sendes første kolonnen (regnr) i listen som parameter til
    funksjonen archive_edit.open_edit. Denne funksjonen slår opp i databasen og henter all data relatert til denne gjenstaden.
    """
    archive_edit.open_edit(root, search, result[result_listbox.curselection()[0]])

print ("cats")
"""
****************************Hovedprogram****************************
"""
# Opprett hovedvindu
root = Tk()

# Oppretter en ledetekster
name_label = Label(root, text="Navn:")
regnr_label = Label(root, text="Regnr:")

# Oppretter tekstfelter brukeren kan søke fra
name = StringVar()  # Definerer en tekstvariabel for tekstfeltet 
name_entry = Entry(root, textvariable=name)
regnr = StringVar()  # Definerer en tekstvariabel for tekstfeltet 
regnr_entry = Entry(root, textvariable=regnr)

# Oppretter en knapp med teksten "Søk", som kaller funksjonen search() ved trykk
search_button = Button(root, text="Søk", command=search)  

# Oppretter listeboks med scrollbar for søkeresultat
scrollbar = Scrollbar(root, orient=VERTICAL)
result_listbox = Listbox(root, yscrollcommand=scrollbar.set)
scrollbar.config(command=result_listbox.yview)
result_listbox.bind('<Double-Button-1>', edit_gjenstand)

# Plasserer widget'ene i vinduet i et rutenett (grid)
name_label.grid(column=0, row=0, padx=2, pady=2)
name_entry.grid(column=1, row=0, padx=2, pady=2)
regnr_label.grid(column=2, row=0, padx=2, pady=2)
regnr_entry.grid(column=3, row=0, padx=2, pady=2)
search_button.grid(column=4, row=0, columnspan=2, padx=2, pady=2)
result_listbox.grid(column=0, row=1, columnspan=5, rowspan=10, sticky=EW)
scrollbar.grid(column=5, row=1, rowspan=10, sticky=NS)

# Lag meny
menubar = Menu(root)
gjenstandMenu = Menu(menubar, tearoff=0)
gjenstandMenu.add_command(label="Registrer ny", command=new_archive)
statisticsMenu = Menu(menubar, tearoff=0)
statisticsMenu.add_command(label="Distribusjon av Materiale", command=view_materiale_statistics) #Endret navn (Berit). 
menubar.add_cascade(label="Gjenstand", menu=gjenstandMenu)
menubar.add_cascade(label="Statistikk", menu=statisticsMenu)
root.config(menu=menubar)

# Starter GUI'et
root.mainloop()
