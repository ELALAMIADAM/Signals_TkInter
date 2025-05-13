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

class MainWindow :
    def __init__(self,parent) :
        self.parent=parent
        self.gui()
        self.actions_binding()

    def gui(self) :
        self.canvas=tk.Canvas(self.parent,width=200,height=150,bg="light yellow")
        self.frame=tk.LabelFrame(self.parent,text="Position Carre (10x10)")
        self.entry=tk.Entry(self.frame)
        self.quit=tk.Button(self.parent,text="Goodbye World", fg="red")
     
    def actions_binding(self) :
       self.entry.bind("<Return>",self.action_entry)
       self.parent.bind("<Control-Z>", self.action_parent)
       self.quit.bind("<Button-1>",self.action_quit)
     
    def action_entry(self,event):
        event.widget.event_generate("<Control-Z>")
    def action_parent(self,event):
        x=int(self.entry.get())
        self.canvas.create_rectangle(x,x,x+10,x+10,fill="blue")
    def action_quit(self,event) :
        self.parent.destroy()

    def layout(self) :
        self.canvas.pack()
        self.frame.pack()
        self.entry.pack()
        self.quit.pack()

if __name__ =="__main__" :
    root=tk.Tk()
    mw=MainWindow(root)
    mw.layout()
    root.mainloop()