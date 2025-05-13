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
def app_exit(event) :
    mw.destroy()
def mouse_location(event,label):
    label.configure(text= "Position X ="+ str(event.x) + ", Y =" + str(event.y))

## Création de l'IHM
def gui(parent) :
    ## arbre des composants graphiques
    frame=tk.Frame(mw,bg="yellow")
    canvas=tk.Canvas(frame,width=200,height=150,bg="light yellow")
    data=tk.Label(frame,text="Mouse Location")
    hello=tk.Label(frame,text="Hello World !",fg="blue")
    button_quit=tk.Button(frame,text="Goodbye World",fg="red")
    ## interaction sur l'IHM : liaison Composant-Evenement-Action
    button_quit.bind("<Button-1>",app_exit)
    ## positionnement des composants  (layout manager)
    frame.pack()
    hello.pack()
    canvas.pack()
    data.pack()
    button_quit.pack()
    # frame.pack(fill="both",expand=1)
    # canvas.pack(side="left")
    # # canvas.pack(fill="both",expand=1,side="left")
    # data.pack(side="right")
    # button_quit.pack(side="bottom")
    ## interaction sur l'IHM : liaison Composant-Evenement-Action
    canvas.bind("<Motion>",lambda event,label=data : mouse_location(event,label))

if __name__ =="__main__" :
    mw=tk.Tk()
    gui(mw)
    mw.mainloop()
    exit(0)
