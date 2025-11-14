print("Adding Data to Dictionary")
print(" ================================")
tuloy = True

empty_dictionary = {}
def print_anime():
    for i,j in empty_dictionary.items():
        print(f"CODE {i} TITLE -- {j}")

def search(key):
    print(f"result {empty_dictionary[key].upper()} on our database")


while tuloy == True:
    keys = input("input keys for this anime --> ")
    value = input("enter anime title -->  ")

    empty_dictionary[keys] = value

    choice = input("Would you like to continue adding anime \ny - yes\nn - No\np - PRINT\ns - SEARCH\n --> ").lower()

    if choice == 'y':
        print("Continuing")
        continue
    elif choice == 'n':
        print("program stops")
        break
    elif choice == 'p':
        print_anime()
        continue
    elif choice == 's':
        code = input("Please input the code of the anime --> ")
        search(code)
        continue
    else:
        print("invalid choice")
        continue
