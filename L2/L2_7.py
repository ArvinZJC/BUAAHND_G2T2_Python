# 第2章.pptx, P54, program that uses the try...except...else...finally statement

i = 10

try:
    j = 30 / (i - 10)
except Exception as e:
    print("Exception:", e)
else:
    print(j)
finally:
    print("The end.")