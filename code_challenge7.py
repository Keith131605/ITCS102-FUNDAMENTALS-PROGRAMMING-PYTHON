print("ODD NUMBER SUMMATION")

odd_num = 0
for x in range(1, 11, 1):
	num = eval(input("Please input a number-> "))
	if num % 2 != 0:
		odd_num += num
print("The total sum of all the odd number is--> ", odd_num)