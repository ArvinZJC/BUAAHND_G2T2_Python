# 第4章.pptx, P28, program that contains a static method


class Test:
    @staticmethod
    def DisplayMessage():
		'''
		Display a message.
		'''
		print("This is a static method.")


user = Test()  # create a Test object and assign it to "user"

# call the specified function in class Test to display a message
user.DisplayMessage()
Test.DisplayMessage()