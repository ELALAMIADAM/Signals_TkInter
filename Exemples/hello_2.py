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
    root.option_readfile("hello.opt")
    label_hello=tk.Label(root,text="Hello World !")
    label_bonjour=tk.Label(root,name="labelBonjour")
    button_quit=tk.Button(root,text="Goodbye World",command=root.destroy)
    label_hello.pack()
    label_bonjour.pack()
    button_quit.pack()
    root.mainloop()
