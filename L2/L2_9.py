# 第2章.pptx, P87 - 94, program that uses tuples

tuple1 = (1, 2, 3, 4) # the values cannot be changed directly

print(tuple1[0])
print(tuple1[3])
print(len(tuple1), end = "\n\n")

list1 = list(tuple1) # change the value in a tuple by converting the tuple to a list
list1.append(5)
tuple1 = tuple(list1)

for index in range(len(tuple1)):
    print(tuple1[index])