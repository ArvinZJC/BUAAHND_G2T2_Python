# 第8章.pptx, P92 & 93, program that uses a Canvas control and function coords

from tkinter import Tk, Canvas

winForm = Tk()

canvas = Canvas(winForm, bg = "white", width = 600, height = 400)
rectangle = canvas.create_rectangle(10, 10, 110, 110, outline = "red", stipple = "gray12", fill = "green")
canvas.coords(rectangle, (40, 40, 200, 100))
canvas.pack()

winForm.mainloop() 