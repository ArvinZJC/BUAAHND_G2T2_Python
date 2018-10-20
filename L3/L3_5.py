#2018.04.15, 第3章.pptx, P41, program with a function receiving variable-length arguments as a dictionary

#print a dictionary
def DisplayDictionary( **dictionary ):
	print( dictionary )

DisplayDictionary( a = 1, b = 2, c = 3 )  #call the specified function to print a dictionary