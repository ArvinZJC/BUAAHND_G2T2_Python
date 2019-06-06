# 第7章.pptx, P60 - 66, program that copies and moves the specified files

import shutil, os

# after all the following operations, it seems that nothing happens to the file "test.txt"
shutil.copy(r"D:\SD\Python\BUAAHND_G2T2_Python\L5\test.txt", r"D:\SD\test_copy.txt")
os.remove("D:\\SD\\Python\\BUAAHND_G2T2_Python\\L5\\test.txt")
shutil.move(r"D:\SD\test_copy.txt", r"D:\SD\Python\BUAAHND_G2T2_Python\L5\test_move.txt")
os.rename(r"D:\SD\Python\BUAAHND_G2T2_Python\L5\test_move.txt", r"D:\SD\Python\BUAAHND_G2T2_Python\L5\test.txt")