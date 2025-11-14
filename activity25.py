from activity25_1 import *
name = input("hi, What is your name->")

print(f"welcome {name}, to my Compiler Program")

isContinue = True

while isContinue == True:
    print("select a Program")
    print("A - Activity1\nB - Activity2\nC - Activity15\n E - Exit")

    choose = input("what program / code would you like to run ->").lower()

    if choose == 'a':
        activity1()
        pass
        continue
    elif choose == 'b':
        activity2()
        pass
        continue
    elif choose == 'c':
        pass
        continue
    elif choose == 'e':
        print("system exit")
        break
    else:
        print("invalid choice")
