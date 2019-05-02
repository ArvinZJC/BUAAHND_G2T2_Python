# 第7章.pptx, P60 - 66, program that copies and moves the specified files

import shutil, os

# after all the following operations, it seems that nothing happens to the file "test.txt"
shutil.copy(r"C:\SD\Python\BUAAHND_G2T2_Python\L5\test.txt", r"C:\SD\test_copy.txt")
os.remove("C:\\SD\\Python\\BUAAHND_G2T2_Python\\L5\\test.txt")
shutil.move(r"C:\SD\test_copy.txt", r"C:\SD\Python\BUAAHND_G2T2_Python\L5\test_move.txt")
os.rename(r"C:\SD\Python\BUAAHND_G2T2_Python\L5\test_move.txt", r"C:\SD\Python\BUAAHND_G2T2_Python\L5\test.txt")