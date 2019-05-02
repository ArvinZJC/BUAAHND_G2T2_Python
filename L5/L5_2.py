# 第6章.pptx, P17 - 19, program that uses lambda statements in a programmer-declared function


def Calculation(selection):
    if selection == 1:
        return lambda x, y : x + y
    
    if selection == 2:
        return lambda x, y : x - y
    
    if selection == 3:
        return lambda x, y : x * y
    
    if selection == 4:
        return lambda x, y : x / y


result1 = Calculation(1)
print("10 + 2 =", result1(10, 2))

result2 = Calculation(2)
print("10 - 2 =", result2(10, 2))

result3 = Calculation(3)
print("10 × 2 =", result3(10, 2))

result4 = Calculation(4)
print("10 ÷ 2 =", result4(10, 2))