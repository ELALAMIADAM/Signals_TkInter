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

from math import pi,sin
from observer import Subject

#class Generator :
class Generator(Subject) :
    def __init__(self,name="X",mag=1.0,freq=1.0,phase=0) :
        Subject.__init__(self)
        self.name=name
        self.mag,self.freq,self.phase=mag,freq,phase
        self.harmonics=1
        self.signal=[]
        self.samples=10
    
    def get_name(self) :
        return self.name
    def set_name(self,name) :
        self.name=name
    def get_frequency(self) :
        return self.freq
    def set_frequency(self,freq) :
        self.freq=freq
    def get_magnitude(self) :
        return self.mag
    def set_magnitude(self,mag) :
        self.mag=mag


    def get_signal(self) :
        return self.signal
    def set_signal(self,signal) :
        if DEBUG :
            print(type(self).__name__+".set_signal()")
        del self.signal[:]
        self.signal=signal
        
    def get_samples(self) :
        return self.samples
    def set_samples(self,samples) :
        self.samples=samples

    def vibration(self,t):
        m,f,p=self.mag,self.freq,self.phase
        harmo=int(self.harmonics)
        sigma=0.0
        for h in range(1,harmo+1) :
            sigma=sigma + (m/h)*sin(2*pi*(f*h)*t-p)
        return sigma

    def generate(self,period=1):
        del self.signal[0:]
        samples=range(int(self.samples)+1)
        psamples = period/self.samples
        for t in samples :
            self.signal.append([t*psamples,self.vibration(t*psamples)])
        self.notify()
        return self.signal

if   __name__ == "__main__" :
    root=tk.Tk()
    model=Generator()
    signal=model.generate()
    print(signal)
    import sqlite3
    connect=sqlite3.connect("signals.db")
    cursor=connect.cursor()
    query="INSERT OR IGNORE INTO signals(signal_id,frequency) VALUES(?,?)"
    to_insert=model.get_name(),model.get_frequency()
    cursor.execute(query,to_insert)
    query="INSERT OR IGNORE INTO samples(signal_id,x,y) VALUES(?,?,?)"
    for value in signal :
        cursor.execute(query,(model.get_name(),value[0],value[1]))
    connect.commit()
    
    # TODO : set samples de 1000
    # TODO : set frequency to 5
    # TODO : update model in signal.db SQLite database 
    #  - UPDATE frequency  in "signals" table on model.get_name()==signal_id
    
    #  - DELETE values from "samples" table on model.get_name()==signal_id
    
    # REDO above INSERT queries  on "samples" table
    # model.set_samples(1000)
    # model.set_frequency(5)
    # signal = model.generate()  
    # query="UPDATE signals SET frequency=? WHERE signal_id=?"
    # cursor.execute(query, (model.get_frequency(), model.get_name()))
    # query="DELETE FROM samples WHERE signal_id=?"
    # cursor.execute(query, (model.get_name(),))

    for value in signal:
        cursor.execute("INSERT OR IGNORE INTO samples(signal_id,x,y) VALUES(?,?,?)", (model.get_name(), value[0], value[1]))
    connect.commit()
    cursor.close()
    connect.close()
 
 

