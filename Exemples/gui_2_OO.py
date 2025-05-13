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
        self.hello=tk.Label(self.parent,text="Hello World !",fg="blue")
        self.quit=tk.Button(self.parent,text="Goodbye World", fg="red")
    
    def actions_binding(self) :
       self.quit.bind("<Button-1>",self.action_quit)
       self.hello.bind("<Button-1>",self.action_hello)

    def action_quit(self,event) :
        self.parent.destroy()
    def action_hello(self,event) :
        print("Coordinates on screen ", event.x_root,event.y_root)
        event.widget.configure(text="x="+str(event.x_root) +"y="+str(event.y_root))
            
    def layout(self) :
       self.hello.pack()
       self.quit.pack()

if __name__ =="__main__" :
    root=tk.Tk()
    mw=MainWindow(root)
    mw.layout()
    root.mainloop()