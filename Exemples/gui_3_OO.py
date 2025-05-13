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
        self.hello=tk.Label(self.parent,text="Hello World !",fg="blue")
        self.canvas=tk.Canvas(self.parent,width=200,height=150,bg="light yellow")
        self.frame=tk.LabelFrame(self.parent,text="Coordonnées")
        self.info=tk.Label(self.frame,text="Dans la Canvas",fg="green")
        self.quit=tk.Button(self.parent,text="Goodbye World", fg="red")
    
    def actions_binding(self) :
       self.quit.bind("<Button-1>",self.action_quit)
       self.hello.bind("<Button-1>",self.action_hello)
       self.canvas.bind("<Motion>",self.action_canvas_move)
       self.canvas.bind("<Leave>",self.action_canvas_leave)

    def action_quit(self,event) :
        self.parent.destroy()
    def action_hello(self,event) :
        event.widget.configure(text="X="+str(event.x_root) +",Y="+str(event.y_root))
    def action_canvas_move(self,event):
        self.info.configure(text= "x="+str(event.x)+ ",y="+ str(event.y))
    def action_canvas_leave(self,event):
        self.info.configure(text= "Dans la Canvas")
            
    def layout(self) :
       self.hello.pack()
       self.canvas.pack()
       self.frame.pack()
       self.info.pack()
       self.quit.pack()


if __name__ =="__main__" :
    root=tk.Tk()
    mw=MainWindow(root)
    mw.layout()
    root.mainloop()