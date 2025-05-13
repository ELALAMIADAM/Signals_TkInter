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
def mouse_press_exit(event) :
    mw.destroy() 
def mouse_enter_exit(event) :
    event.widget.configure(text="X="+str(event.x_root)+" Y="+str(event.y_root))
def mouse_leave_exit(event) :
    event.widget.configure(text="Goodbye World")

def mouse_move_canvas(event,label):
    label.configure(text= "Position x="+str(event.x)+ ", y="+ str(event.y))
def mouse_leave_canvas(event,label):
    label.configure(text= "Mouse location")


# Création de l'IHM
def gui(parent) :
    # arbre des composants graphiques
    canvas=tk.Canvas(parent,width=200,height=150,bg="light yellow")
    data=tk.Label(parent,text="Mouse Location")
    hello=tk.Label(parent,text="Hello World !",fg="blue")
    button_quit=tk.Button(parent,text="Goodbye World", fg="red")
    # positionnement des composants (layout manager)
    hello.pack()
    canvas.pack()
    data.pack()
    button_quit.pack()
    # interaction : liaison Composant-Evenement-Action 
    button_quit.bind("<Button-1>",mouse_press_exit)
    button_quit.bind("<Enter>",mouse_enter_exit)
    button_quit.bind("<Leave>",mouse_leave_exit)
    canvas.bind("<Motion>",lambda event,label=data : mouse_move_canvas(event,label))
    canvas.bind("<Leave>",lambda event,label=data : mouse_leave_canvas(event,label))

if __name__ =="__main__" :
    root=tk.Tk()
    # root.title("CAI : callbacks")
    gui(root)
    root.mainloop()