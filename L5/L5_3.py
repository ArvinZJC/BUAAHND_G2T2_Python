#2018.05.12, 第6章.pptx, P26 & 27, program using filter()

def IsEven( x ):
	return x % 2 == 0

array = filter( IsEven, [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] )

for element in enumerate( array ):
	print( element )