import random
num = random.randint(1,10)
GuessNum = 0
idk = True

while idk == True:
    inp = int(input("Guess a number between 1-10 :"))
    GuessNum += 1

    if inp == num:
        print("Congrats you guess Right!")
        print(f"the right random number is {num} :> ")
        print(f"it took you {GuessNum} tries ")
        break

    else:
        print("Wrong Guess Try Again.")
        continue