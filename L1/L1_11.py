# program that shows the difference between "==" and "is" with 2 group of sets

x = set([1, 2, 3])
y = set([1, 2, 3])
print("x == y:", x == y)
print("x is y:", x is y)
print("id(x) =", id(x))
print("id(y) =", id(y), end = "\n\n")

a = set([1, 2, 3])
b = a
print("a == b:", a == b)
print("a is b:", a is b)
print("id(a) =", id(a))
print("id(b) =", id(b))