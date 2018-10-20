#2018.04.15, 第3章.pptx, P37, program with a programmer-declared function receiving variable-length arguments as a tuple

#print the information of the tuple
def InfoOfTuple( *tuple1 ):
	print( "Its length:", len( tuple1 ) )
	print( "Its values:" )
	
	for index in range( len( tuple1 ) ):
		print( tuple1[ index ] )

InfoOfTuple( 1, 2, 3, 4 )  #call the specified function to print the information of the tuple