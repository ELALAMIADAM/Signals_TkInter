# coding: utf-8
DEBUG=True

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

from models import Generator
from observer import Observer

class Screen(Observer) :
    def __init__(self,parent,bg="white",width=600,height=300):
        self.parent=parent
        self.bg=bg
        self.width,self.height=width,height
        self.tiles=4
        self.signals={}
        self.gui()
        self.create_grid()
        self.actions_binding()
    def get_name(self):
        return "Screen"
    def get_parent(self) :
        return self.parent
    def set_parent(self,parent) :
        self.parent=parent
    def get_tiles(self) :
        return self.tiles
    def set_tiles(self,tiles) :
        self.tiles=tiles
        if self.canvas.find_withtag("grid") :
            self.canvas.delete("grid")
        self.create_grid()
        
    def gui(self) :
        self.canvas=tk.Canvas(self.parent,bg=self.bg,width=self.width,height=self.height)
        
    def actions_binding(self) :
        if DEBUG :
            print(type(self).__name__+".actions_binding()")
        self.canvas.bind("<Configure>",self.resize)
        
    def update(self,subject):
        if subject :
            name=subject.get_name()
            if DEBUG :
                print(type(self).__name__+".update()")
                print(type(subject).__name__+".get_name() : ", name)
            signal=subject.get_signal()
            if signal :
                if name not in self.signals.keys() :
                    self.signals[name]=signal
                else :
                    # del self.signals[name][:]
                    self.signals[name]=signal.copy()
                    self.canvas.delete(name)
                self.plot_signal(name)
            else :
                print("no signal for subject: ",name)
        else :
            print("no subject to observe")
        return

    def plot_signal(self,name):
        if name in self.signals.keys() :
            w,h=self.width,self.height 
            if self.signals[name] and len(self.signals[name]) > 1:
                plot=[(x*w,h*(1/2-y/self.tiles)) for (x,y) in self.signals[name]]
                if name=="X" :
                    color="red"
                else :
                    color="blue"
                self.canvas.create_line(plot,fill=color,smooth=1,width=3,tags=name)
        else :
            print("no signal to plot with name :", name)
        return

    def create_grid(self):
        tile_x=self.width/self.tiles
        for t in range(1,self.tiles+1):
            x =t*tile_x
            self.canvas.create_line(x,0,x,self.height,tags="grid")
            self.canvas.create_line(x,self.height/2-10, x,self.height/2+10,width=3,tags="grid")
        tile_y=self.height/self.tiles
        for t in range(1,self.tiles+1):
            y =t*tile_y
            self.canvas.create_line(0,y,self.width,y,tags="grid")
            self.canvas.create_line(self.width/2-10,y,self.width/2+10,y, width=3,tags="grid")

    def resize(self,event):
        if DEBUG :
            print(type(self).__name__+".resize()")
            print("width,height : ",(event.width,event.height))
        self.width,self.height=event.width,event.height
        # TODO : manage grid and signal refresh in resizing()
        self.canvas.delete("all")
        self.plot_signal('X')
        self.create_grid()


    def layout(self) :
        # self.canvas.pack()
        self.canvas.pack(expand=1,fill="both",padx=20)

if   __name__ == "__main__" :
   root=tk.Tk()
   model=Generator()
   view=Screen(root)
   view.layout()
   # TODO : manage Observer pattern between model and view when generate() is called
   signal=model.generate()
   model.attach(view)
   model.generate()
   second_window = tk.Toplevel(root)
   second_view = Screen(second_window)
   second_view.layout()
   model.attach(second_view)
   model.generate()
   # TODO : manage attachments in layout()
   # TODO : manage grid and signal refresh in resizing()
   # TODO : create a second view on model in a Toplevel Window

   root.mainloop()

   