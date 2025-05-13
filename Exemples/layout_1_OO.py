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

class MainWindow:
    def __init__(self,parent) :
        self.parent=parent
        self.gui()
        self.actions_binding()

    def gui(self) :
        self.canvas=tk.Canvas(self.parent,width=200,height=150,bg="light yellow")
        self.frame=tk.LabelFrame(text="Coordonnées")
        self.data=tk.Label(self.frame,text="Dans la Canvas",fg="green")
        self.hello=tk.Label(self.parent,text="Hello World !",fg="blue")
        self.quit=tk.Button(self.parent,text="Goodbye World", fg="red")
    
    def actions_binding(self) :
       self.quit.bind("<Button-1>",self.action_destroy)
       self.hello.bind("<Button-1>",self.action_info)
       self.canvas.bind("<Motion>",self.action_mouse_move)
       self.canvas.bind("<Leave>",self.action_mouse_leave)

    def action_destroy(self,event) :
        self.parent.destroy()
    def action_info(self,event) :
        print("Coordinates on screen ", event.x_root,event.y_root)
        event.widget.configure(text="x="+str(event.x_root) +"y="+str(event.y_root))
    def action_mouse_move(self,event):
        self.data.configure(text= "Position x="+str(event.x)+ ", y="+ str(event.y))
    def action_mouse_leave(self,event):
        self.data.configure(text= "Dans la Canvas")
            
    def layout(self) :
       self.hello.pack()
       self.canvas.pack(side="left",fill="x",expand=1)
       self.frame.pack(fill="both",expand=1)
       self.data.pack(side="right")
       self.quit.pack(side="bottom")


if __name__ =="__main__" :
    root=tk.Tk()
    mw=MainWindow(root)
    mw.layout()
    root.mainloop()