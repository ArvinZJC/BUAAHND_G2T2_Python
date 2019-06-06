# 第7章.pptx, P57 & 58, program that gets the file status of the specified file

import os, stat, time

fileStatus = os.stat(r"D:\SD\Python\BUAAHND_G2T2_Python\L5\test.txt")
print(fileStatus[stat.ST_SIZE])
print(time.ctime(fileStatus[stat.ST_MTIME]))
print(time.ctime(fileStatus[stat.ST_ATIME]))
print(time.ctime(fileStatus[stat.ST_CTIME]))