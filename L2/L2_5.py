# program that finds prime numbers between 10 and 20

for number in range(10, 21):
    for i in range(2, number):
        if number % i == 0:
            j = number / i
                        
            print("%d = %d × %d" %(number, i, j))
                        
            break
    else:
        print(number, "is a prime number.")