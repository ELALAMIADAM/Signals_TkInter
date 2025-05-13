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

from observer import *

class Model(Subject):
    def __init__(self, names=[]):
        Subject.__init__(self)
        self.__data = names
    def get_data(self):
        return self.__data
    def insert(self,name):
        self.__data.append(name)
        self.notify()               # Observer.update() calls
    def delete(self, index):
        del self.__data[index]
        self.notify()               # Observer.update() calls

class View(Observer):
    def __init__(self,parent):
        self.parent=parent
        self.list=tk.Listbox(parent)
        self.list.configure(height=4)
        self.entry=tk.Entry(parent)

    def update(self,model):         # call by Subject.notify()
        self.list.delete(0, "end")
        for data in model.get_data():
            self.list.insert("end", data)
    def layout(self) :
        self.list.pack()
        self.entry.pack()

class Controller(object):      
    def __init__(self,model,view):  #  needs Model and  View to manage callbacks
        self.model,self.view = model,view
        self.actions_binding()

    def actions_binding(self) :
        self.view.entry.bind("<Return>",self.action_enter)
        self.view.list.bind("<Delete>",self.action_delete)

    def action_enter(self, event):
        data = self.view.entry.get()
        self.model.insert(data)
    def action_delete(self, event):
        for index in self.view.list.curselection():
            self.model.delete(int(index))

if __name__ =="__main__" :
    root=tk.Tk()
    root.title("Men")
    names=["Jean", "John", "Joe"]
    model=Model(names)
    view=View(root)
    model.attach(view)
    model.notify()
    ctrl=Controller(model,view)
    view.layout()

    # top=tk.Toplevel()
    # top.title("Men")
    # view=View(top)
    # model.attach(view)
    # model.notify()
    # ctrl=Controller(model,view)
    # view.layout()

    # top=tk.Toplevel()
    # top.title("Women")
    # names=["Jeanne", "Joanna", "Jeanette"]
    # model=Model(names)
    # view=View(top)
    # model.attach(view)
    # model.notify()
    # ctrl=Controller(model,view)
    # view.layout()

    root.mainloop()
    exit(0)
