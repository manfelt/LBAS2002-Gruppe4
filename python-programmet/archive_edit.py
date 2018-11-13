from tkinter import *
from archive_db import *

"""
Skrevet av: Majid Rouhani
Opprettet: 11.09.2018
Versjon: 1.0

Beskrivesle:
Denne modulen håndterer registrering/oppdatering av data. 
Samler data fra skjermen og bruker db-funksjoner fra modulen archive_db for videre håndtering

-----------------------------------------------------------------------------------------------------------
Endret dato, endret av, versjon
<02.11.2018>, <Berit Gudmundseth>, <1.1> 4.1
<03.11.2018>, <Maria Seljeseth>, <1.2> 4.2
<03.11.2018>, <Simen Myhre>, <1.3> 4,3
-----------------------------------------------------------------------------------------------------------
"""

# Åpner eget vindu for å editere person
def open_edit(root, search, gjenstand_data=None):
    """
    Åpner vindu for registrering av ny gjenstand eller oppdatering av eksisterende gjenstand.
    :param root: referanse til hovedvinduet
    :param search: søke kriteriet (string)
    :param gjenstand_data: dersom data skal oppdateres (liste)
    :return:
    """

    # Definerer aksjon for lagring
    def save_egenskaper():
        """
        Lokal funksjon innhenting av egenskap data fra skjerm.
        Videresender dataene til save_egenskaper_db for lagring
        :return:
        """
        registreringsnr_val = registreringsnr.get()
        fysiske_egenskaper_val = fysiske_egenskaper.get()
        maal_val = maal.get()
        materiale_val = materiale.get()
        tilstand_val = tilstand.get()

        save_egenskaper_db(fysiske_egenskaper_val,
                           maal_val,
                           materiale_val,
                           registreringsnr_val,
                           tilstand_val)


    def save_proveniens():
        """
        Lokal funksjon innhenting av proveniens data fra skjerm.
        Videresender dataene til save_proveniens_db for lagring
        :return:
        """
        registreringsnr_val = registreringsnr.get()
        produsent_val = produsent.get()
        produksjonsaar_val = produksjonsaar.get()
        giver_siste_eier_val = giver_siste_eier.get()
        tidligere_eiere_val = tidligere_eiere.get()
        save_proveniens_db(produsent_val,
                           produksjonsaar_val,
                           registreringsnr_val,
                           giver_siste_eier_val,
                           tidligere_eiere_val)


    def save_gjenstand(kategori_id):
        """
        Lokal funksjon innhenting av gjenstand data fra skjerm.
        Videresender dataene til save_gjenstand_db for lagring

        :param kategori_id: int
        :return:
        """
        registreringsnr_val=registreringsnr.get()
        giver_val = giver.get()
        innlemmet_dato_val = innlemmet_dato.get()
        kommentar_val = ""
        mottatt_av_val = mottatt_av.get()
        plassering_val = plassering.get()
        registrert_av_val = registrert_av.get()
        registrerings_dato_val = registrerings_dato.get()
        navn_val=betegnelse.get()

        save_gjenstand_db(giver_val,
                          innlemmet_dato_val,
                          kategori_id,
                          kommentar_val,
                          mottatt_av_val,
                          navn_val,
                          plassering_val,
                          registrert_av_val,
                          registrerings_dato_val,
                          registreringsnr_val)

    def save_category():
        """
        Lokal funksjon innhenting av kategori data fra skjerm.
        Videresender dataene til save_cateogri_db for lagring
        :return: int
        """
        kategori_id=get_next_category_id()
        kategori_val = kategori.get()
        save_cateogri_db(kategori_id,
                         kategori_val)
        return kategori_id

    #Lage all data
    def save_data():
        """
        Hovedfunksjon for lagring av archive data.
        Kalles videre save_category, save_gjenstand, save_egenskaper og save_proveniens
        :return:
        """
        kategori_id = save_category()

        if registrerings_dato.get() == "":
            messagebox.showerror("Error", "Registreringsnummer må oppgis")
            exit(0)

        save_gjenstand(kategori_id)
        save_egenskaper()
        save_proveniens()
        messagebox.showinfo("Registrering", "Registrering av ny gjenstand er fullført!")
        window.destroy()

    # Definerer aksjon for sletting
    def delete():
        print("delete " + registreringsnr.get())  # Kun logg
        if messagebox.askokcancel("Slett", "Er du sikker på at du vil slette gjenstanden?", parent=window):
            delete_gjenstand(registreringsnr.get())
            window.destroy()  # Lukk dette vinduet
            search()  # Oppdater data i hovedvinduet på nytt siden vi har oppdatert innhold

    # Oppretter et nytt vindu for å editere personinfo
    window = Toplevel(root)
    window.geometry("600x550")

    # Add a title
    window.title("Tussudal Bygdemuseum - Archieve")

    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=2)
    window.columnconfigure(2, weight=2)


    # Logger inndata
    print("open_edit: data=" + str(gjenstand_data))

    registreringsnr = StringVar()
    registrerings_dato = StringVar()
    registrert_av = StringVar()
    innlemmet_dato = StringVar()
    betegnelse = StringVar()
    kategori = StringVar()
    mottatt_av = StringVar()
    giver = StringVar()
    plassering = StringVar()
    materiale = StringVar()
    maal = StringVar()
    tilstand = StringVar()
    fysiske_egenskaper = StringVar()
    produsent = StringVar()
    produksjonsaar = StringVar()
    giver_siste_eier = StringVar()
    tidligere_eiere = StringVar()

    # Hvis vi dobbeltklikket på listen fyller vi ut data'ene vi allerede har
    if gjenstand_data: 
        print("Reading : "+str(gjenstand_data))
        gjenstand = hent_gjenstand(gjenstand_data[0])
        giver.set(gjenstand[0][0])
        innlemmet_dato.set(gjenstand[0][1])
        mottatt_av.set(gjenstand[0][3])
        betegnelse.set(gjenstand[0][4])
        plassering.set(gjenstand[0][5])
        registrert_av.set(gjenstand[0][6])
        registrerings_dato.set(gjenstand[0][7])
        registreringsnr.set(gjenstand[0][8])
        kategori.set(gjenstand[0][9])
        fysiske_egenskaper.set(gjenstand[0][10])
        maal.set(gjenstand[0][11])
        materiale.set(gjenstand[0][12])
        tilstand.set(gjenstand[0][13])
        produsent.set(gjenstand[0][14])
        produksjonsaar.set(gjenstand[0][15])
        giver_siste_eier.set(gjenstand[0][16])
        tidligere_eiere.set(gjenstand[0][17])

        
    # Oppretter widgets og plasserer dem i grid'en
    l1=Label(window, text="Tussudal Bygdemuseum")
    l1.grid(row=0,columnspan=2)
    l1.config(font=("Courier", 22))
    
    
    r=1
    generelt_group = LabelFrame(window, text="Generelt", padx=5, pady=5, borderwidth=2)
    generelt_group.grid(row=r,column=1,sticky=W)
    
    
    #Show an image
    #logo = PhotoImage(file="./bilder/tuddal_bygdemuseum.gif",width=200,height=200)
    #w1 = Label(can1, image=logo).grid(row=0,column=1)
    
    #Registrerings dato
    Label(generelt_group,text="Registreringsdato:",width=25).grid(row=r,column=0,sticky=W)
    Entry(generelt_group,textvariable=registrerings_dato,width=35).grid(row=r,column=1)
    
    #Registrert av
    r+=1
    Label(generelt_group,text="Registrert av:",width=25).grid(row=r,column=0,sticky=W)
    Entry(generelt_group,textvariable=registrert_av,width=35).grid(row=r,column=1)
    
    #Innlemmet dato
    r+=1
    Label(generelt_group,text="Innlemmet dato:",width=25).grid(row=r,column=0,sticky=W)
    Entry(generelt_group,textvariable=innlemmet_dato,width=35).grid(row=r,column=1)
    
    
    identifikasjon_group = LabelFrame(window, text="Identifikasjon", padx=5, pady=5)
    identifikasjon_group.grid(row=r,column=1,sticky=W)
    
    #Identifikasjon
    #r+=1
    #Label(win,text="Identifikasjon").grid(row=r,column=0,sticky=W)
    
    #Registreringsnr
    r+=1
    Label(identifikasjon_group,text="Registreringsnummer:",width=25).grid(row=r,column=0,sticky=W)
    Entry(identifikasjon_group,textvariable=registreringsnr,width=35).grid(row=r,column=1)
    
    #Betegnelse
    r+=1
    Label(identifikasjon_group,text="Betegnelse:",width=25).grid(row=r,column=0,sticky=W)
    Entry(identifikasjon_group,textvariable=betegnelse,width=35).grid(row=r,column=1)
    
    #Kategori
    r+=1
    Label(identifikasjon_group,text="Kategori:",width=25).grid(row=r,column=0,sticky=W)
    Entry(identifikasjon_group,textvariable=kategori,width=35).grid(row=r,column=1)
    
    #Mottatt av
    r+=1
    Label(identifikasjon_group,text="Mottatt av:",width=25).grid(row=r,column=0,sticky=W)
    Entry(identifikasjon_group,textvariable=mottatt_av,width=35).grid(row=r,column=1)
    
    #Giver
    r+=1
    Label(identifikasjon_group,text="Giver:",width=25).grid(row=r,column=0,sticky=W)
    Entry(identifikasjon_group,textvariable=giver,width=35).grid(row=r,column=1)
    
    #Plassering
    r+=1
    Label(identifikasjon_group,text="Plassering:",width=25).grid(row=r,column=0,sticky=W)
    Entry(identifikasjon_group,textvariable=plassering,width=35).grid(row=r,column=1)
    
    fysiske_egenskaper_group = LabelFrame(window, text="Fysiske egenskaper", padx=5, pady=5)
    fysiske_egenskaper_group.grid(row=r,column=1,sticky=W)
    
    
    #Fysiske egenskaper
    #r+=1
    #Label(fysiske_egenskaper_group,text="Fysiske egenskaper").grid(row=r,column=0,sticky=W)
    
    #Materiale
    r+=1
    Label(fysiske_egenskaper_group,text="Materiale:",width=25).grid(row=r,column=0,sticky=W)
    Entry(fysiske_egenskaper_group,textvariable=materiale,width=35).grid(row=r,column=1)
    
    #Mål
    r+=1
    Label(fysiske_egenskaper_group,text="Mål:",width=25).grid(row=r,column=0,sticky=W)
    Entry(fysiske_egenskaper_group,textvariable=maal,width=35).grid(row=r,column=1)
    
    #Tilstand
    r+=1
    Label(fysiske_egenskaper_group,text="Tilstand:",width=25).grid(row=r,column=0,sticky=W)
    Entry(fysiske_egenskaper_group,textvariable=tilstand,width=35).grid(row=r,column=1)
    
    #Fysiske egenskaper
    r+=1
    Label(fysiske_egenskaper_group,text="Fysiske egenskaper:",width=25).grid(row=r,column=0,sticky=W)
    Entry(fysiske_egenskaper_group,textvariable=fysiske_egenskaper,width=35).grid(row=r,column=1)
    
    
    proveniens_group = LabelFrame(window, text="Proveniens", padx=5, pady=5)
    proveniens_group.grid(row=r,column=1,sticky=W)
    
    #Proveniens
    #r+=1
    #Label(win,text="Proveniens").grid(row=r,column=0,sticky=W)
    
    #Produsent
    r+=1
    Label(proveniens_group,text="Produsent:",width=25).grid(row=r,column=0,sticky=W)
    Entry(proveniens_group,textvariable=produsent,width=35).grid(row=r,column=1)
    
    #Produksjonsår
    r+=1
    Label(proveniens_group,text="Produksjonsår:",width=25).grid(row=r,column=0,sticky=W)
    Entry(proveniens_group,textvariable=produksjonsaar,width=35).grid(row=r,column=1)
    
    #Tidligere eiere
    r+=1
    Label(proveniens_group,text="Tidligere eiere:",width=25).grid(row=r,column=0,sticky=W)
    Entry(proveniens_group,textvariable=tidligere_eiere,width=35).grid(row=r,column=1)
    
    #Fysiske Giver/Siste eier. Fjernet giver for å unngå dobbellagring(Berit)
    r+=1
    Label(proveniens_group,text="Siste eier:",width=25).grid(row=r,column=0,sticky=W)
    Entry(proveniens_group,textvariable=giver_siste_eier,width=35).grid(row=r,column=1)
    
    #Lagre data
    r+=1
    button = Button(window, text='Lagre', width=25,command=save_data)
    button.grid(row=r,column=1)

    # Legger til slette-knapp KUN hvis gjenstand data allerede eksisterer
    if gjenstand_data:
        delete_button = Button(window, text="Slett", command=delete)
        delete_button.grid(row=r,column=0)
