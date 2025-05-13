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
from controllers import Control

def menu_file(menubar) :
    menu=tk.Menu(menubar)
    item="Open"
    menu.add_command(label=item, command=lambda name=item: on_file_actions(name))
    item="Exit"
    menu.add_command(label=item, command=lambda name=item: on_file_actions(name))
    menubar.add_cascade(label="File",menu=menu)
    return menu

def menu_help(menubar) :
    menu=tk.Menu(menubar)
    item="About Us"
    menu.add_command(label=item, command=lambda name=item: on_help_actions(name))
    item="About Application"
    menu.add_command(label=item, command=lambda name=item: on_help_actions(name))
    item="About TkInter"
    menu.add_command(label=item, command=lambda name=item: on_help_actions(name))
    menubar.add_cascade(label="Help",menu=menu)

def on_file_actions(name):
    print("on_file_actions()")
    if  name=="Open" :
        open_action()
    elif  name=="Exit" :
        exit(0)
    else :
        print("item: ",name, " non reconnu")

def open_action() :
    print("open_action()")
 
def on_help_actions(name):
    print("on_help_actions()")
    if  name=="About Us" :
        tk.messagebox.showinfo(title=name, message="Contacts",detail="dupond@enib.fr, durand@enib.fr")
    elif name=="About Application" :
        print(name)
    elif  name=="About TkInter" :
        print(name)
    else :
        print("item: ",name, " non reconnu")

if __name__=="__main__" :
    root=tk.Tk()
    root.title("CAI 2025P : TkInter")
    root.option_readfile("main.opt")
    # Model
    model=Generator()          # X signal 

    # View
    frame=tk.LabelFrame(root,name="generator_X") 
    view=Screen(frame)
    frame.pack()
    view.layout()
    signal=model.generate()
    model.attach(view)
    model.generate()

    # Controller
    control=Control(model,view)
    control.layout()

    # # Model
    # model=Generator(name="Y")  # Y signal 
    # model.set_samples(100)
    # model.set_frequency(5)
    # model.attach(view)
    # model.generate()
    # # view.update(model)

    # # View
    # frame=tk.LabelFrame(root,text="Generator: "+model.get_name()) 
    # view=Screen(frame)
    # view.set_tiles(8)
    # model.attach(view)
    # model.generate()
    # frame.pack(expand=1,fill="x",padx=20)
    # view.layout()

    # # Controller
    # control=Control(model,view)
    # frame.pack(expand=1,fill="both",padx=6)
    # frame.pack(side="right")
    # view.layout()
    # control.layout()

    # Menubar 
    menubar=tk.Menu(root) 
    root.config(menu=menubar)
    menu_file(menubar)
    menu_help(menubar)

    root.mainloop()

