# 第5章.pptx, P9 & 14, program that processes the command line parameter

import sys

if len(sys.argv) < 2:
    try:
        sys.exit(1)
    except SystemExit:
        print("Error! No command line parameter entered by the user.")
else:
    print("There is/are %d command line parameter(s) in total." %(len(sys.argv)))
    
    for counter in range(0, len(sys.argv)):
        print("Parameter %d:" %(counter + 1), sys.argv[counter])