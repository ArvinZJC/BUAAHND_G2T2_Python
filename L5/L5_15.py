# 第7章.pptx, P33, program that reads the specified file

file = open("C:\\SD\\Python\\BUAAHND_G2T2_Python\\L5\\test.txt")

while True:
    chunk = file.readline()

    # if no content can be read，then the execution is out of loop
    if not chunk:
        break
    
    print(chunk)

file.close()