# 第2章.pptx, P58 - 85, program that uses lists

list1 = ['C', 'F', 'A', 'D']
print(list1)
print(list1[0])
print(list1[3], end = "\n\n")

list1.append('E')
print(list1, end = "\n\n")

list1.insert(1, 'B')
print(list1, end = "\n\n")

list2 = ['H', 'J', 'G', 'I']
list3 = list1 + list2
print(list3)
list1.extend(list2)
print(list1, end = "\n\n")

del list1[7]
print(list1)
print(list1.index('G'))
print(list1.index('D'), end = "\n\n")

for index in range(len(list1)):
    print(list1[index])

print("\r")

for index, value in enumerate(list1):
    print("list1[%d] = %s" %(index, value))

print("\r")

list1.sort()
list1.reverse()
print(list1, end = "\n\n")

print("-----------")

list4 = [['A', 'B'], ['C', 'D']]

for i in range(len(list4)):
    list5 = list4[i]
    
    for j in range(len(list5)):
        print(list5[j])

print("\r")

for i in range(len(list4)):
    for j in range(len(list4[i])):
        print(list4[i][j])

print("\r")

for index in range(len(list4)):
    print(list4[index])