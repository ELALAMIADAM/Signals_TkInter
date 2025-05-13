# coding: utf-8
import sys
major=sys.version_info.major
minor=sys.version_info.minor
if major==2 and minor==7 :
    import Tkinter as tk
    import tkFileDialog as filedialog
elif major==3 :
    import tkinter as tk
    from tkinter import filedialog
else :
    if __name__ == "__main__" :
        print("Your python version is : ",major,minor)
        print("... I guess it will work !")
    import tkinter as tk
    from tkinter import filedialog 

## Définition des actions, comportements (callbacks)

## Création de l'IHM
def gui(parent) :
    ## arbre des composants graphiques
    frame=tk.Frame(mw,bg="yellow")
    # frame.pack()
    frame.pack(fill="x",expand=1)
    labelNom=tk.Label(frame,text="Nom :")
    labelPrenom=tk.Label(frame,text="Prenom :")
    entryNom=tk.Entry(frame)
    entryPrenom=tk.Entry(frame)
    ## interaction sur l'IHM : liaison Composant-Evenement-Action
    frame.pack()
    labelNom.grid(row=0)
    labelPrenom.grid(row=1)
    entryNom.grid(row=0,column=1)
    entryPrenom.grid(row=1,column=1)
    ## interaction sur l'IHM : liaison Composant-Evenement-Action

if __name__ =="__main__" :
# IHM : creation des composants
    mw=tk.Tk()
    gui(mw)
    mw.mainloop()
    exit(0)