#2018.05.20, 第8章.pptx, P89 & 90, program using a Canvas control to create an image

from tkinter import Tk, Canvas, PhotoImage

winForm = Tk()
winForm.title( "QR Code" )

canvas = Canvas( winForm, bg = "white", width = 600, height = 400 )
pic = PhotoImage( file = r"C:\SD\Python\BUAAHND_G2T2_Python\L6\QR Code.png" )
canvas.create_image( ( 300, 200 ), image = pic )
canvas.pack()

winForm.mainloop()