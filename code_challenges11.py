print("\t\t     *",end='')
for hotdog in range(1,12,1):
    for hamburgir in range(12 , hotdog, -1):
        print("", end='  ')
    for itlog in range(1, hotdog, 1):
        print("*", end = ' ')
    for EGG in range(1, hotdog, 1):
        print("*", end=' ')
    print()

for hotdog in range(1,12,1):
    for hamburgir in range(1, hotdog, 1):
        print("", end='  ')
    for EGG in range(12, hotdog, -1):
        print("*", end=' ')
    for itlog in range(12, hotdog, -1):
        print("*", end = ' ')
    print()
print("\t\t     *",end='')