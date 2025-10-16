madungis = True

while madungis == True:
    confirm = input("Do you wish to continue washing(yes / no) -> ").lower()

    if confirm == 'yes':
        print("resume the cycle")
        continue
    elif confirm == 'no':
        print("the cycle ends")
        break
    else:
        print("invalid")
        continue