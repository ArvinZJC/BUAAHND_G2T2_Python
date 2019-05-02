# 第4章.pptx, P48 - 53, program that contains an abstract method

from abc import ABCMeta, abstractmethod


# parent class Shape
class Shape:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.color = "black"  # set black as the default colour

    @abstractmethod
    def Draw(self):
        pass


# subclass Circle whose parent is class Shape
class Circle(Shape):
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def Draw(self):
        print("Draw Circle: ((%d, %d), %d)" %(self.x, self.y, self.r))


# subclass Line whose parent is class Shape
class Line(Shape):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def Draw(self):
        print("Draw Line: ((%d, %d), (%d, %d))" %(self.x1, self.y1, self.x2, self.y2))


newCircle = Circle(10, 10, 5)  # create a Circle object and assign it to "newCircle"
newLine = Line(10, 10, 20, 20)  # create a Line object and assign it to "newLine"
newCircle.Draw()  # call the specified function in class Circle (parent class Shape) to print the title of the circle
newLine.Draw()  # call the specified function in class Line (parent class Shape) to print the title of the line