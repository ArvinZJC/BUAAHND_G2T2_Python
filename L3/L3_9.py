#2018.04.15, 第4章.pptx, P31, program containing a class method

class Test:   
        #display a message
        @classmethod
        def DisplayMessage( cls ):
                print( "This is a class method of " + str( cls ) + "." )

user = Test()  #create a Test object and assign it to "user"

#call the specified function in class Test to display a message
user.DisplayMessage()
Test.DisplayMessage()