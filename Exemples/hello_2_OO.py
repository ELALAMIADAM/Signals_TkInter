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


class MainWindow :
    def __init__(self,parent) :
        self.parent=parent
        self.gui()
        self.actions_binding()
    def gui(self) :
        """ Creation des composants graphiques"""
        self.hello=tk.Label(self.parent,
                            text="Hello World !",
                            fg="blue")
        self.bonjour=tk.Label(self.parent,
                            name="labelBonjour")
        self.quit=tk.Button(self.parent,
                            text="Goodbye World",
                            fg="red")
    def actions_binding(self) :
        """ Liaison Composant-Evenement-Action """
        self.quit.bind("<Button-1>",self.on_quit_action)
        self.hello.bind("<Leave>",self.on_quit_action)
        self.bonjour.bind("<Enter>",self.on_quit_action)
    def on_quit_action(self,event) :
        """ Action : sortie d'application"""
        self.parent.destroy()
    def layout(self) :
        """ Positionnement des composants """
        self.hello.pack()
        self.bonjour.pack()
        self.quit.pack()

if __name__ =="__main__" :
    root=tk.Tk()
    root.option_readfile("hello.opt")
    mw=MainWindow(root)
    mw.layout()
    root.mainloop()
