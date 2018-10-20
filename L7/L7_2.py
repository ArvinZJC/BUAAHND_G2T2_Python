#2018.05.26, 第8章.pptx, P106-111, program using a Checkbutton control

from tkinter import Tk, IntVar, Checkbutton
from tkinter.messagebox import showinfo

def Feedback():
    if( flag.get() == 1 ):
        showinfo( title = '', message = "Successfully selected." )
    else:
        showinfo( title = '', message = "Successfully deselected." )

winFRM = Tk()

flag = IntVar()
flag.set( 0 )  #set Off as the initial status of the Checkbutton control "checkbutton"
checkbutton = Checkbutton( winFRM, variable = flag, text = "Python", command = Feedback )
checkbutton.pack()

winFRM.mainloop()