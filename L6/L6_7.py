#2018.05.20, 第8章.pptx, P69-72, program using a Canvas control to create polygons

from tkinter import Tk, Canvas

winForm = Tk()

canvas = Canvas( winForm, bg = "white", width = 450, height = 100 )
canvas.create_polygon( 100, 5, 0, 80, 200, 80, outline = "blue", fill = "red", width = 2, smooth = 1 )
canvas.create_polygon( 305, 5, 205, 80, 405, 80, outline = "blue", fill = "red", width = 2 )
canvas.pack()

winForm.mainloop()