# 第8章.pptx, P21 - 39, program that uses Label controls

from tkinter import Tk, Label, PhotoImage

winForm = Tk()
winForm.title("test")
winForm.geometry("700x500")
winForm.minsize(400, 300)
winForm.maxsize(1440, 900)

label1 = Label(winForm, text = "Label 1")
label1.pack()

label2 = Label(winForm, bitmap = "warning")
label2.pack()

pic = PhotoImage(file = r"C:\SD\Python\BUAAHND_G2T2_Python\L6\QR Code.png")
label3 = Label(winForm, image = pic)
label3.bm = pic
label3.pack()

label4 = Label(winForm, fg = "red", bg = "blue", text = "test")
label4.pack()

winForm.mainloop()