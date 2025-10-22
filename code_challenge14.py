name = input("Hi! what is your name - ")
print("+++++++++++++++++++++++++++++++++++++++++++")
print("ODD number compiler, Type '0' to Stop the loop")

advance = True
odd = 0
even =""

while advance == True:
	num = eval(input("Please input a number - "))
	if num == 0:
		print("Loop Stoped")
		break
	
	elif num % 2 == 1:
		print("ODD Number detected")
		odd += num
		even += str(num) + ","
		continue 
	
	else:
		print("EVEN Number")
		continue
	
print(f"Hello {name} the sum of all ODD number you inputed {odd}")
print(f"All the ODD numbers you inputed is {even}")