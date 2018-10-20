#2018.05.26, 第8章.pptx, P124 & 125, program using a LabelFrame control

from tkinter import Tk, LabelFrame, Label, Button

winForm = Tk()

labelFrame = LabelFrame( winForm, height = 300, width = 100, text = "test" )
label = Label( labelFrame, text = "test" )
button = Button( labelFrame, text = "OK" )
labelFrame.pack()
label.pack()
button.pack()

winForm.mainloop();