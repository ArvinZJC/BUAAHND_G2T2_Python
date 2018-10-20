#2018.04.15, 第4章.pptx, P28, program containing a static method

class Test:
        #display a message
        @staticmethod
        def DisplayMessage():
                print( "This is a static method." )

user = Test()  #create a Test object and assign it to "user"

#call the specified function in class Test to display a message
user.DisplayMessage()
Test.DisplayMessage()