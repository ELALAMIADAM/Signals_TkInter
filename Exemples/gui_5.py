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

# Définition des actions, comportements (callbacks)
def app_exit(event) :
    mw.destroy()
def set_value(event):
    event.widget.event_generate("<Control-Z>")
def display(event,canvas,entry):
    x=int(entry.get())
    canvas.create_rectangle(x,x,x+10,x+10,fill="blue")

# Création de l'IHM
def gui(parent) :
    ## arbre des composants graphiques
    canvas=tk.Canvas(mw,width=200,height=150,bg="light yellow")
    frame=tk.Frame(parent)
    label=tk.Label(frame,text = "Value :")
    entry=tk.Entry(frame)
    button_quit=tk.Button(parent,text="Goodbye World", fg="red")
    ## positionnement des composants  (layout manager)
    canvas.pack()
    frame.pack()
    label.pack(side="left")
    entry.pack(side="left")
    button_quit.pack()
    ## interaction sur l'IHM : liaison Composant-Evenement-Action
    entry.bind("<Return>",set_value)
    parent.bind("<Control-Z>",lambda event,canvas=canvas,entry=entry : 
                display(event,canvas,entry))
    button_quit.bind("<Button-1>",app_exit)
 
if __name__ =="__main__" :
    mw=tk.Tk()
    gui(mw)
    mw.mainloop()