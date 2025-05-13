# coding: utf8
import sys
major=sys.version_info.major
minor=sys.version_info.minor
if major==2 and minor==7 :
    import Tkinter as tk
    import tkFileDialog as filedialog
elif major==3 and minor==6 :
    import tkinter as tk
    from tkinter import filedialog
else :
    if __name__ == "__main__" :
        print("Your python version is : ",major,minor)
        print("... I guess it will work !")
    import tkinter as tk
    from tkinter import filedialog 

# Définition des actions, comportements (callbacks)
def callback_info(event) :
    #  user : get data from mouse coordinates
    print("pointer coordinates on screen ", event.x_root,event.y_root)
    #  widget: set widget options
    event.widget.configure(text="x="+str(event.x_root) +"y="+str(event.y_root))

# Création de l'IHM
def gui(parent) :
    # arbre des composants graphiques
    label_hello=tk.Label(parent,text="Hello World !",fg="blue")
    button_quit=tk.Button(parent,text="Goodbye World", fg="red")
    # positionnement des composants (layout manager)
    label_hello.pack()
    button_quit.pack()
    # interaction : liaison Composant-Evenement-Action 
    button_quit.bind("<Button-1>",callback_info)

if __name__ =="__main__" :
    mw=tk.Tk()
    gui(mw)
    mw.mainloop()