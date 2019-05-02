# 第8章.pptx, P95 & 96, program that uses a Canvas control and function move

from tkinter import Tk, Canvas

winForm = Tk()

canvas = Canvas(winForm, bg = "white", width = 150, height = 150)
rectangle = canvas.create_rectangle(10, 10, 110, 110, outline = "red", stipple = "gray12" ,fill = "green")
canvas.create_rectangle(10, 10, 110, 110, outline = "blue")
canvas.move(rectangle, 20, 10)
canvas.pack()

winForm.mainloop() 