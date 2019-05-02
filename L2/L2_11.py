# 第2章.pptx, P113 - 133, program that uses sets

set1 = set("Python")
frozenset1 = frozenset("python")  # the elements cannot be changed directly

print(type(set1))
print(set1)
print(type(frozenset1))
print(frozenset1, end = "\n\n")

for element in set1:
    print(element)

print("\r")

set1.add("3")
print(set1, end = "\n\n")

set2 = set(".6.40")
set1.update(set2)
print(set1, end = "\n\n")

set1.remove("0")
print(set1, end = "\n\n")

if "q" in set1: 
    print('There exists "q".', end = "\n\n")
else:
    print('There does not exist "q".', end = "\n\n")

set1.clear()
print(set1, end = "\n\n")

set1 = set([1, 2, 3])
set3 = set([3, 4])
print(set1 | set3, end = "\n\n")
print(set1.union(set3), end = "\n\n")
print(set1 & set3, end = "\n\n")
print(set1.intersection(set3), end = "\n\n")
print(set1 - set3, end = "\n\n")
print(set1.difference(set3), end = "\n\n")
print(set3 - set1, end = "\n\n")
print(set3.difference(set1), end = "\n\n")
print(set1 ^ set3, end = "\n\n")
print(set1.symmetric_difference(set3))