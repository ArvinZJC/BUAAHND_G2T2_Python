#2018.05.12, 第7章.pptx, P28 & 29, program that reads the specified file

file = open( "C:\\SD\\Python\\BUAAHND_G2T2_Python\\L5\\test.txt" )

while True:
    chunk = file.read( 6 )

    #if no content can be read，then the execution is out of loop
    if not chunk:
        break

    print( chunk )

file.close()  #close the file currently associated with the stream to avoid resource leak