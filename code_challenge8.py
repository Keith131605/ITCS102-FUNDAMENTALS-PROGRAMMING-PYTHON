print("MULTIPLICATION TABLE MAKER")
num = eval(input("Enter a number: "))

print(f"\nMultiplication table for {num}:")
for x in range(1, 11):
    answer = num * x
    print(f"{num} x {x} = {answer}")