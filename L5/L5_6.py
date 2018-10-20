#2018.05.12, 第6章.pptx, P42, program using closure

def Calculation():
    def Add( x, y ):
        return x+y
    
    return Add

Calculation_Add = Calculation()

print( Calculation_Add( 1, 2 ) )