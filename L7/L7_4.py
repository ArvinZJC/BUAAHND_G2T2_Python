#2018.05.26, 第8章.pptx, P118-122, program using a Frame control

from tkinter import Tk, Frame, Label, Button

winForm = Tk()

frame = Frame( winForm, height= 300, width = 100 )
label = Label( frame, text = "test" )
button = Button( frame, text = "OK" )
frame.pack()
label.pack()
button.pack()

winForm.mainloop();