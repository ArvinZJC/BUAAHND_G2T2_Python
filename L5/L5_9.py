# 第6章.pptx, P51 & 52, program that uses a generator


def ModifyList(list1):
    for element in list1:
        yield element + 2


list1 = [1, 2, 3, 4]

for element in ModifyList(list1):
    print(element)