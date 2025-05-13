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

class MainWindow(tk.Frame) :
    def __init__(self,parent) :
        tk.Frame.__init__(self,parent)
        self.parent=parent
        self.gui()
        self.actions_binding()
        self.layout()

    def gui(self) :
        """ Creation des composants graphiques"""
        self.hello=tk.Label(self,
                            text="Hello World !",
                            fg="blue")
        self.quit=tk.Button(self,
                            text="Goodbye World",
                            fg="red")
    def actions_binding(self) :
        """ Liaison Composant-Evenement-Action """
        self.quit.bind("<Button-1>",self.action_destroy)

    def action_destroy(self,event) :
        """ Action : sortie d'application"""
        # self.parent.destroy()
        self.destroy()

    def layout(self) :
        """ Positionnement des composants """
        # self.pack()
        self.hello.pack()
        self.quit.pack()


if __name__ =="__main__" :
    root=tk.Tk()
    mw=MainWindow(root)
    mw.mainloop()