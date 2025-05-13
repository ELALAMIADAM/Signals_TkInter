# coding: utf8
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

from math import cos
# Définition des actions, comportements (callbacks)
def app_exit(event) :
    mw.destroy()
def evaluer(event,entry,label):
    label.configure(text= "Resultat = "+str(eval(entry.get())))

# Création de l'IHM
def gui(parent) :
    # arbre des composants graphiques
    entry=tk.Entry(parent)
    label=tk.Label(parent,text="Resultat")
    button_quit=tk.Button(parent,text="Goodbye World", fg="red")
    # positionnement des composants (layout manager)
    entry.pack()
    label.pack()
    button_quit.pack()
    # interaction sur l'IHM : liaison Composant-Evenement-Action 
    entry.bind("<Return>",lambda event, entry=entry ,label=label: evaluer(event,entry,label))
    button_quit.bind("<Button-1>",app_exit)
 
if __name__ =="__main__" :
    mw=tk.Tk()
    gui(mw)
    mw.mainloop()