# 第2章.pptx, P50, program that calculates the sum of even numbers between 1 and 100:

i = 1
total = 0

for i in range(1, 101):
	if i % 2  == 1:
		continue

	total += i

print("The sum of even numbers between 1 and 100:", total)