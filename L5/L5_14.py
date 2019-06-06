# 第7章.pptx, P31, program that reads the specified file

file = open(r"D:\SD\Python\BUAAHND_G2T2_Python\L5\test.txt", 'r')
list1 = file.readlines()
file.close()

print(list1)