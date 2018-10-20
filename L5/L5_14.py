#2018.05.12, 第7章.pptx, P31, program that reads the specified file

file = open( r"C:\SD\Python\BUAAHND_G2T2_Python\L5\test.txt", 'r' )
list1 = file.readlines()
file.close()  #close the file currently associated with the stream to avoid resource leak

print( list1 )