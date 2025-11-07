def greeter(name):
    print(f"Hi {name}, kamusta kana? ")

greeter("pikolo")
greeter("kamiyas")
greeter("coco")
greeter("paminta")

def summation(x):
    sum = 0
    for y in range(x, 0, -1):
        sum += y
    print(f"the sum of {x} is {sum}")