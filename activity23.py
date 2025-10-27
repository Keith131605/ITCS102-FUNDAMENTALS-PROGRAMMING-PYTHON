months = ['Jan','Feb','Mar','Apr','May','Jyn','Jul']

months.append('Aug')
print(months)
months.pop()
print(months)
months.append('Aug')
print(months)
months.reverse()
print(months)

for m in months:
    print(f"{m}, 2025")

fullname = 'Keith James Glorioso'

for i in fullname[0:]:
    print(i)

another = list(fullname)

another.reverse()

print(another)