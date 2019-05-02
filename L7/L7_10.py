# 第8章.pptx, P155 & 156, program that uses a Scale control

from tkinter import Tk, Scale

winForm = Tk()

scale = Scale(winForm, from_ = 0, to = 100, resolution = 1, orient = "horizontal")
scale.pack()

winForm.mainloop()