# -*- coding: utf-8 -*-
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
        print("Your python version is : ", major, minor)
        print("... I guess it will work !")
    import tkinter as tk
    from tkinter import filedialog 

from observer import *

class Model(Subject):
    def __init__(self):
        super().__init__()
        self.value = tk.IntVar()
        self.value.set(0)
    def increase(self):
        self.value.set(self.value.get()+1)
        self.notify()
    def decrease(self):
        self.value.set(self.value.get()-1)
        self.notify()
    def reset(self):
        self.value.set(0)
        self.notify()

class View(Observer):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.frame=tk.Frame(self.parent)
        self.display = tk.Label(self.frame)
        self.btn_increase = tk.Button(self.frame, text="Increase")
        self.btn_decrease = tk.Button(self.frame, text="Decrease")
        self.btn_reset = tk.Button(self.parent, text="Reset")
    
    def update(self,model) :
        pass

    def layout(self) :
        self.frame.pack()
        self.btn_increase.pack(side="left")
        self.display.pack(side="left")
        self.btn_decrease.pack(side="left")
        self.btn_reset.pack()

class Controller:
    def __init__(self, model,view):
        self.model=model
        self.view=view
        self.callbacks()

    def callbacks(self) :
        # to display model data in view
        self.view.display.config(textvariable=self.model.value)
        self.view.btn_increase.config(command=self.model.increase)
        self.view.btn_decrease.config(command=self.model.decrease)
        self.view.btn_reset.config(command=self.model.reset)

if __name__ == "__main__":
    root=tk.Tk()
    model=Model()
    view=View(root)
    ctrl=Controller(model,view)
    view.layout()
    root.mainloop()