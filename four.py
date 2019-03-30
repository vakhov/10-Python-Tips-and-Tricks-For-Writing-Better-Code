# Enumerate

names = ['Alex', 'Dima', 'Petr', 'Lena']

index = 0
for name in names:
    print(index, name)
    index += 1

# #######################################

for index, name in enumerate(names):
    print(index, name)

for index, name in enumerate(names, start=1):
    print(index, name)
