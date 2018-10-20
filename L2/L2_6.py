#2018.04.15, program using the while...else statement

counter = 0

while counter < 5:
    print( counter, "is less than 5." )
    
    counter += 1  #there is no "++" or "--" in Python
else:
    print( counter, "is not less than 5." )