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
    item="Save"
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
    elif  name=="Save" :
        save_action()
    elif  name=="Exit" :
        exit(0)
    else :
        print("item: ",name, " non reconnu")

def save_action():
    print("save_action()")
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()

    try:
        signal_id = model.get_name()
        frequency = model.get_frequency()
        magnitude = model.get_magnitude()
        samples = model.get_samples()
        
        # Update the signals table
        
        cursor.execute("""
            UPDATE signals
            SET frequency = ?, amplitude = ?, phase = ?
            WHERE signal_id = ?
        """, (frequency, magnitude, samples, signal_id))
        # print(signal_id, frequency, magnitude, samples)


        # Insert into the samples table
        
        query = "INSERT OR IGNORE INTO samples(signal_id, x, y) VALUES(?,?,?)"
        for value in signal:
            # print("value : ", value)
            cursor.execute(query, (model.get_name(), value[0], value[1]))
 
        
        # Commit the changes
        
        conn.commit()
        print("Data updated and inserted successfully.")
    
    except sqlite3.Error as e:
        print("SQLite error:", e)
    
    finally:
        # Close the connection
        cursor.close()
        conn.close()
        
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
    control.layout("left")
    # control.layout("right")
    # Save database on sqlite3
    import sqlite3
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    magnitude = model.get_magnitude() if model.get_magnitude() is not None else 0.0
    samples = model.get_samples() if model.get_samples() is not None else 0
    cursor.execute(
        "INSERT OR IGNORE INTO signals(signal_id,frequency,amplitude,phase) VALUES(?,?,?,?)",
        (model.get_name(), model.get_frequency(), magnitude,samples)
    )

    query="INSERT OR IGNORE INTO samples(signal_id,x,y) VALUES(?,?,?)"
    for value in signal :
        cursor.execute(query,(model.get_name(),value[0],value[1]))
    conn.commit()

    cursor.close()
    conn.close()
    
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

