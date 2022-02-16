import tkinter as tk
from tkinter import WORD
import pyperclip
import time
import datetime
import pyautogui as pya
import threading
import tkinter.scrolledtext as scrolledtext

#CONSTANTS
COLORE_FINESTRA = "#856ff8"

#W_DOCUMENTO = 60
#W_LISTA = 30
#W_BOTTONI = 10
#W_SPAZIO = 20

#H_DOOCUMENTO = 40
#H_ETICHETTA = 5

W_DOCUMENTO = 70
W_LISTA = 20
W_BOTTONI = 45
W_SPAZIO = 5

H_DOOCUMENTO = 25
H_ETICHETTA = 5

#X_DOCUMENTO =20
#X_BOTTONI = X_DOCUMENTO + W_DOCUMENTO*11 - W_SPAZIO
#X_TEDESCO = X_DOCUMENTO + W_DOCUMENTO*11 + W_BOTTONI + 2* W_SPAZIO
#X_INGLESE = X_DOCUMENTO + W_DOCUMENTO*11 + W_BOTTONI + W_LISTA*12 + 3* W_SPAZIO


X_DOCUMENTO =20
X_BOTTONI = X_DOCUMENTO + W_DOCUMENTO*9 -45
X_TEDESCO = X_BOTTONI+ W_BOTTONI
X_INGLESE = X_TEDESCO + W_LISTA*10 +  W_SPAZIO-20

Y_ETICHETTE = 20
Y_CONTENUTO = 60

i = 1

def carica_documento_remaining():
   carica_documento("DOCUMENTO", documento)
   carica_documento("INGLESE", paroleE)
   carica_documento("TEDESCO", paroleT)

def salva_documento_remaining():
   salva_documento("DOCUMENTO", documento)
   salva_documento("INGLESE", paroleE)
   salva_documento("TEDESCO", paroleT)

def parola_ingles_in_lista():
    global lista
    lista = paroleE
    parola_in_lista()

def parola_tedes_in_lista():
   global lista
   lista = paroleT
   parola_in_lista()

def parola_in_lista():
   global lista
   pya.hotkey('ctrl', 'c')
   corri_controllo()

def carica_documento(nome, campo):
    campo.delete(1.0, tk.END)   
    lettore = open("./" + nome)
    linee = lettore.readlines()
    for linea in linee:
        campo.insert(tk.END, linea)
    lettore.close()

def salva_documento(nome,campo):
    scrittore = open("./" + nome,"w")
    linee = campo.get('1.0', 'end').split('\n')
    for linea in linee:
        scrittore.write(linea)
        scrittore.write('\n')
    scrittore.close()

def dividi_parole():
    linee = documento.get('1.0', 'end').split()
    documento.delete(1.0, tk.END)
    for linea in linee:
        documento.insert(tk.END, linea.replace('.','').replace(',','').replace('"','').replace("'",'').replace("“","").replace("”","") + '\n')

def combina_parole():
    lineeI = paroleE.get('1.0', 'end').split('\n')
    lineeT = paroleT.get('1.0', 'end').split('\n')
    documento.delete(1.0, tk.END)   
    i=0
    for linea in lineeT:
        if (len(linea)> 0):
            documento.insert(tk.END, linea + "," + lineeI[i] + '\n')
        i+=1

def filo_controllo():
    global lista
    time.sleep(0.1)
    clipboard = root.clipboard_get()
    lista.focus_set()
    lista.insert(tk.END, clipboard + "\n")

##interfaccia per principale
def inizializza_finestra(colore_finestra):
    global root, documento, lista, paroleE, paroleT

    root = tk.Tk()
    root.title('This is my day')
 #   root.geometry("1600x900+0+0")
    root.geometry("1020x520+0+0")
    root.configure(bg = colore_finestra)

    tk.Label(root, text="DOCUMENTO", bg = colore_finestra).place(x=X_DOCUMENTO, y=Y_ETICHETTE)
    documento = scrolledtext.ScrolledText(root, height=H_DOOCUMENTO, width=W_DOCUMENTO)
    documento.place(x=X_DOCUMENTO, y=Y_CONTENUTO)
    documento.config(wrap=WORD)

    tk.Label(root, text="TEDESCO", bg=colore_finestra).place(x=X_TEDESCO, y=Y_ETICHETTE)
    paroleT = scrolledtext.ScrolledText(root, height=H_DOOCUMENTO, width=W_LISTA, undo=True)
    paroleT.place(x=X_TEDESCO , y = Y_CONTENUTO)
    paroleT.configure(background="light blue", foreground="red")

    tk.Label(root, text="INGLESE", bg = colore_finestra).place(x=X_INGLESE, y=Y_ETICHETTE)
    paroleE = scrolledtext.ScrolledText(root, height=H_DOOCUMENTO, width=W_LISTA)
    paroleE.place(x=X_INGLESE, y=Y_CONTENUTO)
    paroleE.configure(background="yellow", foreground="red")

    tk.Button(root, text='PI', command=parola_ingles_in_lista).place(x=X_BOTTONI, y=Y_CONTENUTO)
    tk.Button(root, text='A', command=carica_documento_remaining).place(x=X_BOTTONI, y=Y_CONTENUTO + 50)
    tk.Button(root, text='S', command=salva_documento_remaining).place(x=X_BOTTONI, y=Y_CONTENUTO + 100)
    tk.Button(root, text='PT', command=parola_tedes_in_lista).place(x=X_BOTTONI, y=Y_CONTENUTO + 150)
    tk.Button(root, text='CP', command=combina_parole).place(x=X_BOTTONI, y=Y_CONTENUTO + 200)
    tk.Button(root, text='D', command=dividi_parole).place(x=X_BOTTONI, y=Y_CONTENUTO + 200)
#    paroleE['font'] = ('consolas', '12')

def corri_finestra():
    tk.mainloop()

def metti_a_fuoco():
    root.deiconify()
    root.attributes('-topmost', 1)

def corri_controllo():
    x = threading.Thread(target=filo_controllo)
    x.setDaemon(True)
    x.start()

inizializza_finestra(COLORE_FINESTRA)
corri_finestra()

 

