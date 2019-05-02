# 第8章.pptx, P135, program that uses a Menu control

from tkinter import Tk, Menu


def Feedback():
    print("I am a menu.")


winForm = Tk()

menu = Menu(winForm)
menuFile = Menu(menu)

for item in ["New", "Open", "Save", "Save As", "Exit"]:
    menuFile.add_command(label = item, command = Feedback)

menuFile.add_separator()
menuFile.add_checkbutton(label = "(test)")
menu.add_cascade(label = "File", menu = menuFile)
menu.add_command(label = "Help", command = Feedback)
winForm["menu"] = menu

winForm.mainloop()