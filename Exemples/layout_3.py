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
    var = tk.StringVar()
    msg = tk.Message(mw, textvariable=var, bg="yellow",relief="ridge")
    var.set("Place : \n options de  positionnement  de widgets ")
    okButton=tk.Button(mw,text="OK")
    ## interaction sur l'IHM : liaison Composant-Evenement-Action
    ## positionnement des composants  (layout manager)
    msg.place(relx=0.5,rely=0.5,relwidth=0.75,relheight=0.50,anchor="center")
    okButton.place(relx=0.5,rely=1.05,in_=msg,anchor="n")
 
if __name__ =="__main__" :
    mw=tk.Tk()
    mw.title("Layout Manager : Place")
    gui(mw)
    mw.mainloop()
    exit(0)
