# 第2章.pptx, P41, program that uses the if...elif...else statement

import datetime

str1 = "Today is "
dateAndTime = datetime.datetime.now()

if dateAndTime.weekday() == 0:
	str1 += "Monday."
elif dateAndTime.weekday() == 1:
    str1 += "Tuesday."
elif dateAndTime.weekday() == 2:
    str1 += "Wednesday."
elif dateAndTime.weekday() == 3:
    str1 += "Thursday."
elif dateAndTime.weekday() == 4:
    str1 += "Friday."
elif dateAndTime.weekday() == 5:
    str1 += "Saturday."
else:
    str1 += "Sunday."

print(str1)