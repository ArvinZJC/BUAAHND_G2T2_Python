#2018.05.12, 第7章.pptx, P36, program that reads the specified file

file = open( "C:\\SD\\Python\\BUAAHND_G2T2_Python\\L5\\test.txt" )

for line in file:
    print( line )

file.close()  #close the file currently associated with the stream to avoid resource leak