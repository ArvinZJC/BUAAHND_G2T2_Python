#2018.04.15, 第3章.pptx, P33, program with a programmer-declared function containing an argument with default value

#display a message
def DisplayMessage( message, times = 1 ):
	print( message * times )

#call the specified function to display a message
DisplayMessage( "Hello" )
DisplayMessage( "Python! ", 3 )