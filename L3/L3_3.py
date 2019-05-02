# 第3章.pptx, P33, program with a programmer-declared function containing an argument with default value


def DisplayMessage(message, times = 1):
	'''
	Display a message.
	'''
	print(message * times)


# call the specified function to display a message
DisplayMessage("Hello")
DisplayMessage("Python! ", 3)