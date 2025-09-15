num = eval(input("input number - "))

result = 1
for n in range(num, 0, -1):
    #print(n)
    result *= n

print("The factorial is ",result)