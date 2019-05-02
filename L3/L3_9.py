# 第4章.pptx, P31, program that contains a class method


class Test:   
	@classmethod
	def DisplayMessage(cls):
		'''
		Display a message.
		'''
		print("This is a class method of " + str(cls) + ".")


user = Test()  # create a Test object and assign it to "user"

# call the specified function in class Test to display a message
user.DisplayMessage()
Test.DisplayMessage()