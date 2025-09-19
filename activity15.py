odd_sum = 0
for hotdog in range(1, 11, 1):
    num = eval(input(f"{hotdog} - enter a number:"))

    if num % 2 == 1:
        odd_sum += num

print(f"The sum of all the ODD numbers given is {odd_sum}")        