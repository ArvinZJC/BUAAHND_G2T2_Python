# 第7章.pptx, P52, program that reads the specified file and writes to it

file = open(r"C:\SD\Python\BUAAHND_G2T2_Python\L5\test.txt", "r+")

file.truncate(12)
str1 = file.readline()
print(str1)

file.seek(5)
file.truncate()
file.seek(0)
str2 = file.readline()
print(str2)

file.write(" Python!\nHello Python!\nHello Python!")
file.seek(0)
str3 = file.readline()
print(str3)

file.close()