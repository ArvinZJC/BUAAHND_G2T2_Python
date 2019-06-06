# 第7章.pptx, P49 & 50, program that writes to the specified file and reads it

file = open(r"D:\SD\Python\BUAAHND_G2T2_Python\L5\test.txt", "w+")

position1 = file.tell()
file.write("Hello Python!\nHello Python!\nHello Python!")
position2 = file.tell()
print(position1)
print(position2, end = "\n\n")

file.seek(0)  # set the file pointer to the start
position3 = file.tell()
str2 = file.readline()
position4 = file.tell()
print(position3)
print(str2)
print(position4)

file.close()