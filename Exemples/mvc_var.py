# -*- coding: utf-8 -*-
# https://profjahier.github.io/html/NSI/tkinter/variable_controle.html

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

from random import choice

class WhatToDo :
    def __init__(self,parent) :
        self.parent=parent
        self.todo = ["Work", "Eat", "Sleep","Walk"]
        self.model=tk.StringVar()
        self.model.set(choice(self.todo))
        self.gui()
        self.callbacks()

    def gui(self) :
        self.frame=tk.LabelFrame(self.parent,text="ToDo")
        self.view=tk.Label(self.frame,textvariable=self.model)
        self.ctrl=tk.Button(self.frame, text="Choice")
 
    def callbacks(self) :
        self.ctrl.bind("<Button-1>",self.cb_todo)

    def cb_todo(self,event):
        self.model.set(choice(self.todo))

    def layout(self) :
        self.frame.pack(expand=1,fill="x")
        self.ctrl.pack(side="left")
        self.view.pack(side="right")

class ShareValue :
    def __init__(self,parent) :
        self.parent=parent
        self.model=tk.IntVar()
        self.model.set(1)
        self.gui()
        self.callbacks()

    def gui(self) :
        self.frame=tk.LabelFrame(root,text="Change Value")
        self.view=tk.Label(self.frame,textvariable=self.model)
        self.ctrl_increase=tk.Button(self.frame, text="Increase")
        self.ctrl_decrease=tk.Button(self.frame, text="Decrease")

    def callbacks(self) :
        self.ctrl_increase.bind("<Button-1>", self.increase)
        self.ctrl_decrease.bind("<Button-1>", self.decrease)

    def increase(self,event):
        value=self.model.get()+1
        self.model.set(value)
    def decrease(self,event):
        value=self.model.get()-1
        self.model.set(value)

    def layout(self) :
        self.frame.pack(expand=1,fill="x")
        self.ctrl_increase.pack(side="left",expand=1,fill="x")
        self.view.pack(side="left",expand=1,fill="x")
        self.ctrl_decrease.pack(side="left",expand=1,fill="x")

if __name__ =="__main__" :
    root=tk.Tk()
    root.title("CAI : Variable de controle (MVC)")
    root.geometry('300x200+500+500')

    mvc=WhatToDo(root)
    mvc.layout()

    mvc=ShareValue(root)
    mvc.layout()

    root.mainloop()