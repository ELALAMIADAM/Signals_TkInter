# coding: utf-8
import sys
import sqlite3
import tkinter as tk
from tkinter import simpledialog
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
    item="load"
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
        save_signal()
    elif  name=="load" :
        load_signal()
    elif  name=="Exit" :
        exit(0)
    else :
        print("item: ",name, " non reconnu")



def save_signal():
    # Prompt the user for the signal name
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    signal_id = simpledialog.askstring("Signal Name", "Enter the name of the signal:")

    if not signal_id:
        print("Signal save operation canceled. No name provided.")
        return

    # Get signal data from the model
    magnitude = model.get_magnitude() if model.get_magnitude() is not None else 0.0
    samples_nb = model.get_samples() if model.get_samples() is not None else []
    frequency = model.get_frequency()

    # Save the signal to the database
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    try:
        # Insert into signals table (signal_id is auto-generated)
        cursor.execute("""
            INSERT INTO signals (signal_id, frequency, magnitude, samples_nb)
            VALUES (?, ?, ?, ?)
        """, (signal_id, frequency, magnitude, samples_nb))
        
        # Insert into samples table
        query = "INSERT INTO samples (signal_id, x, y) VALUES (?, ?, ?)"
        for value in signal:
            cursor.execute(query, (signal_id, value[0], value[1]))


        
        conn.commit()
        print(f"Signal '{signal_id}' saved successfully.")
    except sqlite3.Error as e:
        print("SQLite error:", e)
    finally:
        cursor.close()
        conn.close()


def load_signal():
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT signal_id FROM signals")
        signals = cursor.fetchall()

        if not signals:
            print("No signals found in the database.")
            return

        # Display available signal IDs to the user
        signal_options = "\n".join([str(signal[0]) for signal in signals])


        # Prompt the user to select a signal by ID
        top = tk.Toplevel()
        top.withdraw()  # Hide the root window
        selected_signal_id = simpledialog.askstring(
            "Select Signal", f"Enter the Signal ID from the following options:\n\n{signal_options}"
        )

        if not selected_signal_id:
            print("Signal load operation canceled. No ID provided.")
            return

        # Fetch the selected signal's metadata
        cursor.execute("""
            SELECT signal_id, frequency, magnitude, samples_nb
            FROM signals
            WHERE signal_id = ?
        """, (selected_signal_id,))
        signal = cursor.fetchone()

        if not signal:
            print(f"Signal with ID '{selected_signal_id}' not found.")
            return

        signal_id, frequency, magnitude, samples_nb = signal

        model.set_samples(samples_nb)
        model.set_magnitude(magnitude)
        model.set_frequency(frequency)
        control.magn.set(magnitude)
        control.samp.set(samples_nb)
        control.freq.set(frequency)

        print(samples_nb)
        print(model.get_magnitude())
        print(model.get_frequency())
        model.generate()  


    except sqlite3.Error as e:
        print("SQLite error:", e)
    finally:
        cursor.close()
        conn.close()



def open_action() :
    print("open_action()")
 
def on_help_actions(name):
    print("on_help_actions()")
    if  name=="About Us" :
        tk.messagebox.showinfo(title=name, message="Contacts",detail="a3elalam@enib.fr, m2mohama@enib.fr")
    elif name=="About Application" :
        description = (
        "This application is a graphical user interface (GUI) for visualizing, controlling, "
        "and saving data related to harmonic vibratory motion models. It is built using the "
        "TkInter library and follows design patterns such as Observer and MVC to separate the "
        "model, view, and controller components.\n\n"
        "Features include:\n"
        "- Visualization of signals and their parameters (frequency, magnitude, samples_nb, etc.)\n"
        "- Real-time updates using the Observer pattern\n"
        "- Database integration for saving and loading signal data\n"
        "- User-friendly controls for modifying signal properties\n"
        "- Support for multiple views and signal comparisons\n"
        "- Menu options for file operations and application information\n"
        "- Customizable interface with configuration options\n"
        "- Signal plotting using Matplotlib\n\n"
        "This application is designed for educational purposes to demonstrate good programming "
        "practices and the use of design patterns in GUI development."
        )
        tk.messagebox.showinfo("Application Information", description)

    elif  name=="About TkInter" :
        description = (
        "TkInter is the standard Python library for creating graphical user interfaces (GUIs). "
        "It provides a robust and easy-to-use framework for building desktop applications. "
        "TkInter is built on top of the Tk GUI toolkit, which is cross-platform and works on Windows, macOS, and Linux.\n\n"
        "Key Features of TkInter:\n"
        "- Widgets: Includes a variety of widgets such as buttons, labels, text boxes, sliders, menus, and more.\n"
        "- Layout Management: Supports multiple layout managers (pack, grid, and place) for arranging widgets.\n"
        "- Event Handling: Provides mechanisms to handle user interactions like button clicks, key presses, etc.\n"
        "- Customization: Allows customization of widget properties such as colors, fonts, and styles.\n"
        "- Extensibility: Can be extended with additional libraries like ttk for themed widgets and Matplotlib for plotting.\n\n"
        "TkInter is widely used for educational purposes, prototyping, and lightweight desktop applications. "
        "It is included with Python, making it accessible without requiring additional installations."
        )
        tk.messagebox.showinfo("About TkInter", description)

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

