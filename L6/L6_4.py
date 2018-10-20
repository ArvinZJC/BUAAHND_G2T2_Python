#2018.05.20, 第8章.pptx, P55-58, program using a Canvas control to create lines

from tkinter import Tk, Canvas

winForm = Tk()

canvas = Canvas( winForm, bg = "white", width = 200, height = 100 )
canvas.create_line( 10, 10, 100, 80, width = 2, dash = 7 )
canvas.create_line( 50, 10, 100, 10, arrow = "none" )
canvas.create_line( 50, 20, 100, 20, arrow = "first" )
canvas.create_line( 50, 30, 100, 30, arrow = "last" )
canvas.create_line( 50, 40, 100, 40, arrow = "both" )
canvas.pack()

winForm.mainloop()