#2018.05.12, 第6章.pptx, P29, program using reduce()

from functools import reduce

def Add( x, y ): 
    return x + y

total = reduce( Add,( 2, 4, 6, 8, 10 ) )

print( total )