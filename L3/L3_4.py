# 第3章.pptx, P37, program with a programmer-declared function receiving variable-length arguments as a tuple


def InfoOfTuple(*tuple1):
	'''
	Print the information of the tuple.
	'''
	print("Its length:", len(tuple1))
	print("Its values:")
	
	for index in range(len(tuple1)):
		print(tuple1[index])


InfoOfTuple(1, 2, 3, 4)  # call the specified function to print the information of the tuple