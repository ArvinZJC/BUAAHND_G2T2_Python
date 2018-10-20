#2018.05.12, 第6章.pptx, P32-36, program using zip()

list1 = [ 1, 2, 3 ]
list2 = [ 4, 5, 6 ]
list3 = [ 4, 5, 6, 7, 8, 9 ]
list4 = zip( list1, list2 )
list5 = zip( list1, list3 )
list6 = zip( list2, list3 )
list7 = zip( *list6 )

for element in list4:
    print( element )

print()

for element in list5:
    print( element )

print()

for element in list7:
    print( element )