#2018.05.20, 第8章.pptx, P73-78, program using a Canvas control to create ovals

from tkinter import Tk, Canvas

winForm = Tk()

canvas = Canvas( winForm, bg = "white", width = 450, height = 100 )
canvas.create_oval( 10, 10, 100, 50, outline = "blue", fill = "red", width = 2 )
canvas.create_oval( 105, 10, 195, 100, outline = "blue", fill = "red", width = 2 )
canvas.pack()

winForm.mainloop()