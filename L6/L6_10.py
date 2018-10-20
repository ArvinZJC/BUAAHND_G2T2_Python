#2018.05.20, 第8章.pptx, P87 & 88, program using a Canvas control to create a bitmap

from tkinter import Tk, Canvas

winForm = Tk()

canvas = Canvas( winForm, bg = "white", width = 100, height = 100 )
dictionary = { 1 : "error", 2 : "info", 3 : "question", 4 : "hourglass" }

for key in dictionary:
    canvas.create_bitmap( (20 * key, 20 * key ), bitmap = dictionary[ key ] )

canvas.pack()

winForm.mainloop()