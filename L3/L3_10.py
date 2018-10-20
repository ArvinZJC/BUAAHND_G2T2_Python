#2018.04.15, 第4章.pptx, P34, program using isinstance()

class Test:
    def __init__( self ):
        self.str1 = "Hello Python!"

user = Test()  #create a Test object and assign it to "user"
print( isinstance( user, Test ) )

list1 = [ 1, 2, 3, 4 ]
print( isinstance( list1, list ) )