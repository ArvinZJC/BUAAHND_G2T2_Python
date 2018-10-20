#2018.04.15, 第3章.pptx, P46-61, program containing some built-in functions

print( abs( -1 ) )
print( round( 80.23456, 2 ) )
print( pow( 2, 3 ) )
print( divmod( 8, 3 ), end = "\n\n" )

str1 = "hello World"
print( str1.upper() )
print( str1.lower() )
print( str1.swapcase() )
print( str1.capitalize() )
print( str1.title(), end = "\n\n" )

str2 = "Hello World"
print( str2.find( 'l' ) )
print( str2.index( 'o' ) )
print( str2.rfind( 'l' ) )
print( str2.rindex( 'o' ) )
print( str2.count( 'o' ) )
print( str2.replace( ' ', '*' ) )
print( str2.ljust( 15, '*' ) )
print( str2.rjust( 15, '*' ) )
print( str2.center( 15, '*' ) )
print( str2.zfill( 15 ), end = "\n\n" )

str3 = "\tHello\n"
print( str3.strip() )
print( str3.lstrip() )
print( str3.rstrip() )
print( str3.expandtabs( 4 ), end = "\n\n" )

str4 = "PythonStringFunction"
print( str4.startswith( 't' ) )
print( str4.endswith( 'd' ) )
print( str4.isalnum() )
print( str4.isalpha() )
print( str4.isupper() )
print( str4.islower() )
print( str4.isdigit(), end = "\n\n" )

str5 = "Hello World Python"
str6 = "Hello World\nPython"
str7 = "--"
list1 = str5.split( ' ' )
list2 = str6.splitlines()
list3 = [ "Hello", "World", "Python" ]
print( list1 )
print( list2 )
print( str7.join( list3 ), end = "\n\n" )

str8 = "print"
number = 10
list4 = [ 1, 2, 3 ]
help( list4 )
help( str8 )
print( type( str8 ) )
print( type( number ) )
print( type( list4 ) )