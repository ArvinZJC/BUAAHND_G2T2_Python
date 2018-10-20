#2018.04.15, 第3章.pptx, P14, program that shows the scope of a variable

x = 100  #the global variable "x"

#print the value of a local variable
def setNumber():
        x = 10  #the local variable "x"
        print( x )

setNumber()  #call the specified function to print the value of a local variable
print( x )