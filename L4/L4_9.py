# 第5章.pptx, P47 - 49, program that imports module decimal

from decimal import Decimal, getcontext

number1 = Decimal("1.0") / Decimal(3)
number2 = Decimal("1.0") / Decimal("0.6")

print(type(number1), type(number2))
print(number1)
getcontext().prec = 6  # influence the result of the following one statement
print(number1 / 3)
print(Decimal(str(number2)).quantize(Decimal("0.00")))