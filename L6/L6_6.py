#2018.05.20, 第8章.pptx, P64-68, program using a Canvas control to create arcs

from tkinter import Tk, Canvas

winForm = Tk()

canvas = Canvas( winForm, bg = "white", width = 200, height = 100 )
canvas.create_arc( 10, 10, 100, 100, outline = "blue", fill = "red", width = 2, start = 0, extent = 359 )
canvas.create_arc( 105, 10, 195, 80, outline = "blue", fill = "red", width = 2, stipple = "gray12", start = 0, extent = 30 )
canvas.pack()

winForm.mainloop()