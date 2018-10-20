#2018.05.20, 第8章.pptx, P40-50, program using Button controls

from tkinter import Tk, Button, PhotoImage
from tkinter.messagebox import showinfo

def Feedback():
    showinfo( title = "", message = "Surprise!" )

winForm = Tk()
winForm.title( "test" )

button1 = Button( winForm, text = "Surprise?", command = Feedback )
button1.pack()

pic = PhotoImage( file = r"C:\SD\Python\BUAAHND_G2T2_Python\L6\QR Code.png" )
button2 = Button( winForm, command = Feedback, image = pic )
button2.bm = pic
button2.pack()

button3 = Button( winForm, text = "Surprise?", command = Feedback, bd = 5 )
button3.pack()

button4 = Button( winForm, text = "Surprise?", command = Feedback, state = "disabled" )
button4.pack()

winForm.mainloop();