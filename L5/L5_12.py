# 第7章.pptx, P27, program that reads the specified file

# it can be simplified as "file = open("test.txt")" if the file is in the same path as this Python file
file = open("D:\\SD\\Python\\BUAAHND_G2T2_Python\\L5\\test.txt")
str1 = file.read()
file.close()  # close the file currently associated with the stream to avoid resource leak or any other problems

print(str1)