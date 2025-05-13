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

if __name__ =="__main__" :
    root=tk.Tk()
    label_hello=tk.Label(root,
                         text="Hello World !",fg="blue")
    button_quit=tk.Button(root,
                          text="Goodbye World",fg="red",
                          command=root.destroy)
    label_hello.pack()
    button_quit.pack()
    root.mainloop()
