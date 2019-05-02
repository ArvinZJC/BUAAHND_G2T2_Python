# 第8章.pptx, P149 - 153, program that uses Radiobutton controls

from tkinter import Tk, IntVar, Radiobutton

winForm = Tk()

flag = IntVar()
flag.set(1)  # set the initial value of the variable "flag" to 1 to make the following 2 Radiobutton controls a group
radiobutton1 = Radiobutton(winForm, text = "Male", value = 1, variable = flag)
radiobutton2 = Radiobutton(winForm, text = "Female", value = 0, variable = flag)
radiobutton1.pack()
radiobutton2.pack()

winForm.mainloop()