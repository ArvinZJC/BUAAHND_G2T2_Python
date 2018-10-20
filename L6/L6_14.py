﻿#2018.05.20, 第8章.pptx, P97 & 98, program using a Canvas control and delete()

from tkinter import Tk, Canvas

winForm = Tk()

canvas = Canvas( winForm, bg = "white", width = 150, height = 150 )
rectangle = canvas.create_rectangle( 10, 10, 110, 110, outline = "red", stipple = "gray12", fill = "green" )
canvas.create_rectangle( 10, 10, 110, 110, outline = "blue" )
canvas.delete( rectangle )
canvas.pack()

winForm.mainloop()