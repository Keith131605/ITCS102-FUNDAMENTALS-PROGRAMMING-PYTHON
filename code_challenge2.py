amount = eval(input("Enter amount to deposit: "))

n1000 = amount // 1000
amount = amount % 1000

n500 = amount // 500
amount = amount % 500

n200 = amount // 200
amount = amount % 200

n100 = amount // 100
amount = amount % 100

n50 = amount // 50
amount = amount % 50

n20 = amount // 20
amount = amount % 20

n10 = amount // 10
amount = amount % 10

n5 = amount // 5
amount = amount % 5

n1 = amount // 1
amount = amount % 1

print("\nHere is the breakdown, using PH denomination:")

print(n1000 , "- 1000")

print(n500 ,"- 500")

print(n200 ,"- 200")

print(n100 ,"- 100")

print(n50 ,"- 50")

print(n20 ,"- 20")

print(n10 ,"- 10")

print(n5 ,"- 5")

print(n1 ,"- 1")

print(n1 ,"- 1")