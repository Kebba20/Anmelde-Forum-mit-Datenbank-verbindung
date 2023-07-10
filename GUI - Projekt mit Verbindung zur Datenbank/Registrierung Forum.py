from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import maskpass
import mysql.connector




# Verbindung zu MySQL Datenbank
dbase = mysql.connector.connect(
    host ="localhost",
    password = "Database85@fg",
    user = "root",
    database = "datenbank")
mycursor = dbase.cursor()
#print(dbase)

#password = "Database85@fg"



# Die Funktion sendet die Daten in die Datenbank und die Datenbank speichert sie.
def Add():
    idnummer = ID_Entry.get()
    nachname = entry.get()
    vorname = entry2.get()
    geburtsdatum = entry3.get()
    geburtsort = entry4.get()
    email = entry5.get()
    gender = geschlecht.get()
    output_school = eingabe_sch_o_uni.get()
    class_class = klassenstufe.get()
    studium_choice = sg.get()
    benutzer_name = benutzername_entry.get()
    passswort = passwort_entry.get()

    sql = "INSERT INTO student (idstudent, nachname, vorname, geburtsdatum, geburtsort, email, geschlecht, schuleoderuni, klasse, studiengang, benutzername, passwort) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    value = (idnummer, nachname, vorname, geburtsdatum, geburtsort, email, gender, output_school, class_class, studium_choice, benutzer_name, passswort )
    mycursor.execute(sql, value)
    

    dbase.commit()
    





root = Tk()
root.title("Registrierung") # Titel des Fensters
root.geometry('925x500+300+200') # Anpassung des Fensters
root.configure(bg= "skyblue")
root.resizable(False, True) # Fenster nicht vergrößbar

#Überschrift
ueberschrift = Label(text = "Registrierung",font = 'Helvetica 24 bold', fg = "black", bg = "skyblue")
ueberschrift.place(x = 330, y = 5)

# ID-Label
ID = Label(text = "ID :", bg = "skyblue")
ID.place(x = 70, y = 80)

#Eingabefeld ID
ID_Entry = Entry()
ID_Entry.place(x = 110, y = 80)

#Label des Nachnamens
label1 = Label(text="Nachname :",bg = "skyblue")#, bg="red") # Textausgabe
label1.place(x=190, y=150) # Platzierung des Textes

#Eingabefeld des Nachnamens
entry = Entry(width = 50) # Eingabefeld
entry.place(x=300, y=150)



#Label des Vornamens
label2 = Label(text="Vorname :", bg ="skyblue")
label2.place(x=200, y=180)


#Eingabefeld des Vornamens
entry2 = Entry(width = 50)
entry2.place(x=300, y=180)

#Label des Geburtsdatums
label3 = Label(text="Geburtsdatum :", bg ="skyblue") # Textausgabe
label3.place(x=170, y=210) # Platzierung des Textes

#Eingabefeld des Geburtsdatums
entry3 = Entry(width = 50) # Eingabefeld
entry3.place(x=300, y=210)

#Label des Geburtsortes
label4 = Label(text="Geburtsort :", bg ="skyblue") # Textausgabe
label4.place(x=190, y=240) # Platzierung des Textes


#Eingabefeld des Geburtsortes
entry4 = Entry(width = 50) # Eingabefeld
entry4.place(x=300, y=240)

#E-Mail Label 
label5 = Label(text="E-Mail :", bg ="skyblue") # Textausgabe
label5.place(x=210, y=270) # Platzierung des Textes


#E-Mail Eingabefeld
entry5 = Entry(width = 50) # Eingabefeld
entry5.place(x=300, y=270)


# Auswahl des Geschlechts
geschlecht = ttk.Combobox(values=["Keine Angabe","männlich","weiblich"], width = 17, state ="r")
geschlecht.place(x = 300, y = 100)
geschlecht.set("Geschlecht wählen")


#Label Schule oder Uni
sch_o_uni = Label(text = "Schule / Uni :", bg = "skyblue")
sch_o_uni.place(x = 180, y = 300)

#Eingabefeld Schule oder Uni
eingabe_sch_o_uni = Entry(width = 50)
eingabe_sch_o_uni.place(x = 300, y = 300)


# Label - Klassenstufe
label6 = Label(text="Klassenstufe :", bg ="skyblue") # Textausgabe
label6.place(x=180, y=330) # Platzierung des Textes


#Auswahl der Klassenstufe
klassenstufe = ttk.Combobox(values=["Keine Angabe","5","6","7","8","9","10","11","12","13","14"], width = 17, state ="r")
klassenstufe.place(x = 300, y = 330)
klassenstufe.set("")

# Label - Studiengang
label7 = Label(text="Studiengang :", bg ="skyblue") # Textausgabe
label7.place(x=180, y=360) # Platzierung des Textes

#Auswahl der Studiengänge
sg = ttk.Combobox(values=["Keine Angabe",""], width = 17, state ="r")
sg.place(x = 300, y = 360)
sg.set("")






#Bestätigungs - Button
image_check_icon = PhotoImage(file = "C:\\Users\\moham\\OneDrive\\Desktop\\ALogo\\green.png" )
check_button = Button(root, image = image_check_icon, command = Add)
check_button.place(x = 500 ,y = 70 )






#Benutername - Label
benutzername_label = Label(root, text = "Benutzername :", bg = "skyblue")
benutzername_label.place(x=180, y=390) # Platzierung des Textes

#Eingabefeld - Benutername
benutzername_entry = Entry(width = 50) # Eingabefeld
benutzername_entry.place(x=300, y=390)

#Label - Passwort
passwort_label = Label(root, text = "Passwort :", bg = "skyblue")
passwort_label.place(x=180, y=420) # Platzierung des Textes

#Eingabefeld - Passwort
passwort_entry = Entry(width = 50) # Eingabefeld
passwort_entry.place(x=300, y=420)







root.mainloop()