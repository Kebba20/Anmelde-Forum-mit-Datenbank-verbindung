from tkinter import *
from tkinter import messagebox
#import maskpass
import mysql.connector


root = Tk()
root.title("Login") # Titel des Fensters
root.geometry('925x500+300+200') # Anpassung des Fensters
root.configure(bg= "#fff")
root.resizable(False, False) # Fenster nicht vergrößbar


#Verbindung zur MySQL Datenbank
dbase = mysql.connector.connect(
    host ="localhost",
    password = "Database85@fg",
    user = "root",
    database = "datenbank")
#mycursor = dbase.cursor()
#print(dbase)




#Die Funktion prüft ob die Daten benutername und code also(passowort) in der Datenbank
#vorhanden sind. Wenn ja, wird der Zugang gewährt.
#Wenn nicht vorhanden wird der Zugang nicht gewährt.
def logs():
    mycursor = dbase.cursor()
    sql = "SELECT * FROM student WHERE BINARY benutzername = '%s' AND passwort = '%s' " % (username.get(), code.get())
    mycursor.execute(sql)
    
    if mycursor.fetchone():
        messagebox.showinfo("Zugang gewährt! ", "Ihr Login wurde erfolgreich abgeschlossen!")
        
        
        #print("Zugang erfolgreich gewährt!")
        

    else:
        messagebox.showerror("Eingabe ungültig!", "Sie haben Ihre Daten falsch eingeben oder Sie sind nicht registriert!") 







#Bild
img = PhotoImage(file = "C:\\Users\\moham\\OneDrive\\Desktop\\helpStudies Projekt\\login.png")# Bild eingefügt
Label(root, image=img, bg= "white").place (x =50, y = 50)


frame = Frame(root, width = 350, height = 350, bg = "white")
frame.place(x = 480, y = 70)

#Überschrift
heading = Label(frame, text = "Anmeldung",font = 'Helvetica 24 bold', fg = "#57a1f8", bg = "white")
heading.place(x = 100, y = 5)

#Die Funktion sorgt dafür das beim Anklicken auf dem Feld das Wort "Benutzername" verschwindet.
def on_enter(e):
    username.delete(0, "end")

def on_leave(e):
    name = username.get()
    if name == "":
        username.insert(0,"Benutzername")


#Label und Eingabefeld für Benutzername
username = Entry(frame, width = 25, fg = "black", border = 0, bg = "white")# Eingabefeld wird erstellt
username.place(x = 30, y = 80) #Platzierung des Eingabefeldes
username.insert(0,"Benutzername")
username.bind("<FocusIn>",on_enter)
username.bind("<FocusOut>",on_leave)# Das Wort "Benutername" wird ausgeblendet nach dem man anfängt zu schreiben"


#Linie für Eingabefeld-Benutzername
Frame(frame, width = 295, height = 2, bg = "black").place (x =25, y = 107)# Linie


# #Die Funktion sorgt dafür das beim Anklicken auf dem Feld das Wort "Passwort" verschwindet.
def namen_eingabe(e):
    code.delete(0, "end")

def name_weg(e):
    name = code.get()
    if name == "":
        code.insert(0,"Passwort")



##Label und Eingabefeld für Passwort
code = Entry(frame, width = 25, fg = "black", border = 0, bg = "white")
code.place(x = 30, y = 150)
code.insert(0,"Passwort")
code.bind("<FocusIn>",namen_eingabe)# Das Wort "Passwort" wird ausgeblendet nach dem man drauf klickt."
code.bind("<FocusOut>",name_weg)


#Linie für Eingabefeld-Passwort
Frame(frame, width = 295, height = 2, bg = "black").place (x =25, y = 177)



# Anmelde-Button
Button(frame,width = 39,pady = 7, text = "Anmelden", bg = "#57a1f8",fg = "white",border = 0, command = logs).place(x= 35, y = 204)
label = Label(frame, text = "Haben Sie Ihr Passwort vergessen oder möchten es Sie ändern?", fg = "black", bg = "white")
label.place(x = 5,y = 265)

#Die Funktion öffnet ein neues Fenster für die Änderung des Passworts 
def neues_Fenster():
    screen = Toplevel(root)# 2tes Fenters
    screen.title("Änderung des Passworts")
    screen.geometry("925x500+300+200")
    screen.configure(bg= "white")
    screen.resizable(False, False) # Fenster nicht vergrößbar
    
    #Bild
    img = PhotoImage(file = "C:\\Users\\moham\\OneDrive\\Desktop\\helpStudies Projekt\\help2.png")# Bild eingefügt
    Label(screen, image=img, bg= "white").place (x =50, y = 50)
    
    #Überschrift
    heading2 = Label(screen, text = "Änderung des Passworts!",font = 'Helvetica 24 bold', fg = "#57a1f8", bg = "white")
    heading2.place(x = 250, y = 5)
    
    dbasee = mysql.connector.connect(
    host ="localhost",
    password = "Database85@fg",
    user = "root",
    database = "datenbank")
    
    def enter_vornamee(e):
        vornamee.delete(0, "end")

    def leave_vornamee(e):
        name = vornamee.get()
        if name == "":
            vornamee.insert(0,"Vorname")
            
            
    def enter_nachnamee(e):
        nachnamee.delete(0, "end")

    def leave_nachnamee(e):
        name = nachnamee.get()
        if name == "":
            nachnamee.insert(0,"Nachname")
            
            
            
    def enter_email(e):
        email.delete(0, "end")

    def leave_email(e):
        name = email.get()
        if name == "":
            email.insert(0,"E-Mail")          
    
    # Die Funktion prüft, ob die Daten Vorname, Nachname, Email, in der Datenbank vorhanden sind.
    def bestätigung():
        mycursor1 = dbasee.cursor()
        sql1 = "SELECT * FROM student WHERE BINARY vorname = '%s' AND nachname = '%s' AND email = '%s' " % (vornamee.get(), nachnamee.get(), email.get())
        mycursor1.execute(sql1)
    
        if mycursor1.fetchone():
            #def app():
                #bildschirm = Toplevel(root)
                #bildschirm.title("Änderung des Passworts")
                #bildschirm.geometry("925x500+300+200")
                #bildschirm.configure(bg= "white")
                #bildschirm.resizable(False, False)
                
            messagebox.showinfo("E-Mail Sendung! ", "Vielen Dank!" "\n" "Wir werden Ihnen einen Link zur der Passwort Änderung senden!")
            #print("Zugang erfolgreich gewährt!")
        

        else:
            messagebox.showerror("Eingabe ungültig!", "Sie haben Ihre Daten falsch eingeben oder Sie sind nicht registriert!") 

    
    
    
    
    
    
    #Label und Eingabefeld für Vorname, Nachname und E-Mail.   
    
    vornamee = Entry(screen, width = 25, fg = "black", border = 0, bg = "white")# Eingabefeld wird erstellt
    vornamee.place(x = 555, y = 97) #Platzierung des Eingabefeldes
    vornamee.insert(0,"Vorname")
    vornamee.bind("<FocusIn>",enter_vornamee)
    vornamee.bind("<FocusOut>",leave_vornamee)# Das Wort "Vorname" wird ausgeblendet nach dem man anfängt zu schreiben"
    
    
    nachnamee = Entry(screen, width = 25, fg = "black", border = 0, bg = "white")# Eingabefeld wird erstellt
    nachnamee.place(x = 555, y = 160) #Platzierung des Eingabefeldes
    nachnamee.insert(0,"Nachname")
    nachnamee.bind("<FocusIn>",enter_nachnamee)
    nachnamee.bind("<FocusOut>",leave_nachnamee)# Das Wort "Nachname" wird ausgeblendet nach dem man drauf klickt zu schreiben"
    
    
    
    email = Entry(screen, width = 25, fg = "black", border = 0, bg = "white")# Eingabefeld wird erstellt
    email.place(x = 555, y = 228) #Platzierung des Eingabefeldes
    email.insert(0,"E-Mail")
    email.bind("<FocusIn>",enter_email)
    email.bind("<FocusOut>",leave_email)# Das Wort "Email" wird ausgeblendet nach dem man drauf klickt zu schreiben"
  
    #Eingabefeld - Linien
    Frame(screen, width = 295, height = 2, bg = "black").place (x =550, y = 120)# Linie
    Frame(screen, width = 295, height = 2, bg = "black").place (x =550, y = 183)# Linie
    Frame(screen, width = 295, height = 2, bg = "black").place (x =550, y = 250)# Linie
    
    #Bestätiguns-Button
    Button(screen,width = 35,pady = 7, text = "Bestätigen", bg = "#57a1f8",fg = "white",border = 0, command = bestätigung).place(x= 570, y = 290)
    

    
    
    
    screen.mainloop()


# Button-Passwort ändern
passwort_ändern = Button(frame,width = 15, text ="Passwort ändern", border = 0, bg = "white",cursor = "hand2", fg = "blue", command = neues_Fenster)
passwort_ändern.place(x = 130,y = 290)








root.mainloop