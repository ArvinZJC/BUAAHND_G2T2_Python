# 第3章.pptx, P22 & 23, program with a formal parameter and an actual parameter


def IncreaseValue(number):
    '''
    Print the decimal address and the value of a formal parameter.
    '''
    number += 1
    print('The decimal address of the formal parameter "number":', id(number), "\nIts value:", number, end = "\n\n")


x = 10  # the actual parameter "x"

IncreaseValue(x)  # call the specified function to print the decimal address and the value of a formal parameter
print('The decimal address of the actual parameter "x":', id(x), "\nIts value:", x)