# 第3章.pptx, P14, program that shows the scope of a variable

x = 100 # the global variable "x"


def setNumber():
    '''
    Print the value of a local variable.
    '''
    x = 10 # the local variable "x"
    print(x)


setNumber() # call the specified function to print the value of a local variable
print(x)