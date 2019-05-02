# 第4章.pptx, P25, program that contains a static variable


class Test:
    counter = 0
    
    # constructor
    def __init__(self):
        Test.counter += 2

    # destructor
    def __del__(self):
        Test.counter -= 1


user = Test()  # create a Test object and assign it to "user"

user.counter += 1
print(user.counter)
print(Test.counter, end = "\n\n")

del user
print(Test.counter)