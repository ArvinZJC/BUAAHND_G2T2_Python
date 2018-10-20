#2018.04.30, 第5章.pptx, P42-46, program importing module random

import random

print( random.random() )
print( random.uniform( 1, 3 ) )
print( random.randint( 0, 99 ) )
print( random.randrange( 0, 101, 2 ) )
print( random.choice( "jklhgy&#&*()%^@" ) )
print( random.sample( "jklhgy&#&*()%^@", 4 ), end = "\n\n" )

list1 = [ 1, 2, 3, 4, 5, 6 ]

random.shuffle( list1 )
print( list1 )