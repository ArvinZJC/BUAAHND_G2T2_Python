#2018.05.20, 第8章.pptx, P5-20, program using module tkinter.messagebox

from tkinter import Tk
from tkinter.messagebox import askquestion, YES, askyesno, showinfo, askokcancel, askretrycancel, showwarning, showerror

winForm = Tk()
selection1 = askquestion( title = "Question 1", message = "Is this the first time your program using Python?" )

if selection1 == YES:
    showinfo( title = "", message = "Thank you for choosing Python!" )
else:
    selection2 = askyesno( title = "Question 2", message = "Do you like Python?" )
    
    if selection2 == True:
        showinfo( title = "", message = "^_^" )
    else:
        selection3 = askokcancel( title = "", message = "Thank you for answering this short questionnaire!" )

        if selection3 == True:
            showinfo( title = "", message = "Python will continue improving herself." )
        else:
            selection4 = askretrycancel( title = "", message = "Error occurs." )
            
            if selection4 == True:
                showwarning( title = "Warning", message = "Processing..." )
            else:
                showerror( title = "Error", message = "Error still exists." )

winForm.mainloop()