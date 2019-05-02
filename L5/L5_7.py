# 第6章.pptx, P43, program that uses recursion


def Factorial(n):
    if n == 1:
        return 1
    
    return n * Factorial(n - 1)


print(Factorial(5))