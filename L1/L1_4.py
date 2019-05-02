# 第2章.pptx, P9, program that uses function id to get the decimal address of a variable

str1 = "AAA"
print("str1 = " + str1)
print("The decimal address of \"str1\": %d" %(id(str1)))
print("\r")

str2 = str1
print("str2 = " + str2)
print("The decimal address of \"str2\": %d" %(id(str2)), end = "\n\n")

str1 = "aaa"
print("str1 = " + str1 )
print("The decimal address of \"str1\": %d" %(id(str1))) 
print("str2 = " + str2 )  # the change on the value of the viarable "str1" will not affect the value of the variable "str2"
print("The decimal address of \"str2\": %d" %(id(str2)))