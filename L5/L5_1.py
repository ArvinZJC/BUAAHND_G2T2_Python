# 第6章.pptx, P13 & 16 & 23, program that uses lambda statements

total = lambda num1, num2, num3 : num1 + num2 + num3
print(total(1, 2, 3), end = "\n\n")

array1 = [(lambda x : x ** 2), (lambda x : x ** 3), (lambda x : x ** 4)]
print(array1[0](2), array1[1](2), array1[2](2), end = "\n\n")

array2 = map(lambda x, y : x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
for element in enumerate(array2):
    print(element)