#2018.05.26, 第8章.pptx, P155 & 156, program using a Scale control

from tkinter import Tk, Scale

winForm = Tk()

scale = Scale( winForm, from_ = 0, to = 100, resolution = 1, orient = "horizontal" )
scale.pack()

winForm.mainloop()