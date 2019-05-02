# 第6章.pptx, P42, program that uses closure


def Calculation():
    def Add(x, y):
        return x + y
    
    return Add


Calculation_Add = Calculation()

print(Calculation_Add(1, 2))