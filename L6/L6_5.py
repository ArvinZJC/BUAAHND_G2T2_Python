# 第8章.pptx, P59 - 63, program that uses a Canvas control to create rectangles

from tkinter import Tk, Canvas

winForm = Tk()

canvas = Canvas(winForm, bg = "white", width = 300, height = 100)
canvas.create_rectangle(10, 10, 100, 80, outline = "blue", fill = "red", width = 2)
canvas.create_rectangle(105, 10, 195, 80, outline = "blue", fill = "white", width = 2, dash = 7)
canvas.create_rectangle(200, 10, 290, 80, outline = "blue", fill = "red", width = 2, stipple = "gray12")
canvas.pack()

winForm.mainloop()