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

from math import *

class MainWindow :
    def __init__(self,parent) :
        self.parent=parent
        self.gui()
        self.actions_binding()

    def gui(self) :
        self.frame=tk.LabelFrame(self.parent,text="Calculatrice")
        self.entry=tk.Entry(self.frame)
        self.label=tk.Label(self.frame,text="Resultat")
        self.quit=tk.Button(self.parent,text="Goodbye World", fg="red")
     
    def actions_binding(self) :
       self.quit.bind("<Button-1>",self.action_quit)
       self.entry.bind("<Return>", self.action_entry)
        
    def action_quit(self,event) :
        self.parent.destroy()
    def action_entry(self,event):
       self.label.configure(text="Resultat = "+str(eval(self.entry.get())))

    def layout(self) :
        self.frame.pack()
        self.entry.pack()
        self.label.pack()
        self.quit.pack()


if __name__ =="__main__" :
    root=tk.Tk()
    mw=MainWindow(root)
    mw.layout()
    root.mainloop()