#2018.05.12, 第6章.pptx, P43, program using recursion

def Factorial( n ):
    if n == 1:
        return 1
    
    return n * Factorial( n - 1 )

print( Factorial( 5 ) )