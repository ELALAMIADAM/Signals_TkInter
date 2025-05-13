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

from models import Generator
from views import Screen

class Control :
    def __init__(self,model,view):
        self.model=model
        self.view=view
        self.gui()
        self.actions_binding()

    def gui(self):
        parent=self.view.get_parent()
        self.frame=tk.LabelFrame(parent,text=self.model.get_name()) 
        self.scale_frequency()
        self.scale_samples()
        self.scale_magnitude()

        # Magnitude
    def scale_magnitude(self) :
        self.magn=tk.IntVar()
        self.magn.set(self.model.get_magnitude())
        self.scale_magn=tk.Scale(self.frame,variable=self.magn,
                             label="Magnitude",
                             orient="horizontal",length=250,
                             from_=0,to=100,tickinterval=10
                            #  ,resolution=0.1
                             )
    def on_magnitude_action(self,event):
        if  self.model.get_magnitude() != self.magn.get() :
            self.model.set_magnitude(self.magn.get())
            self.model.generate()
            print("magnitude : ",self.magn.get())     
        # Samples

    def scale_samples(self) :
        self.samp=tk.IntVar()
        self.samp.set(self.model.get_samples())
        self.scale_samp=tk.Scale(self.frame,variable=self.samp,
                             label="Samples",
                             orient="horizontal",length=250,
                             from_=0,to=100,tickinterval=10)
    def on_samples_action(self,event):
        if  self.model.get_samples() != self.samp.get() :
            self.model.set_samples(self.samp.get())
            self.model.generate()
    # frequency
    def scale_frequency(self) :
        self.freq=tk.IntVar()
        self.freq.set(self.model.get_frequency())
        self.scale_freq=tk.Scale(self.frame,variable=self.freq,
                             label="Frequency",
                             orient="horizontal",length=250,
                             from_=0,to=100,tickinterval=10)


    def on_frequency_action(self,event):
        if  self.model.get_frequency() != self.freq.get() :
            self.model.set_frequency(self.freq.get())
            self.model.generate()


    def actions_binding(self) :
        self.scale_freq.bind("<B1-Motion>",self.on_frequency_action)
        self.scale_samp.bind("<B1-Motion>",self.on_samples_action)
        self.scale_magn.bind("<B1-Motion>",self.on_magnitude_action)

    def layout(self,side="top") :
        self.frame.pack(side=side)
        self.scale_freq.pack()
        self.scale_samp.pack()
        self.scale_magn.pack()

if   __name__ == "__main__" :
   root=tk.Tk()
   # Model
   model=Generator()
   # View
   view=Screen(root)
   view.layout()
   model.attach(view)
   
   # TODO : manage Observer pattern between model and view when generate() is called
   # Controller
   # TODO : modify Controller to visualize model frequency changes in view  
   control=Control(model,view)
   control.layout("left")

   
   model.generate()
   root.mainloop()

