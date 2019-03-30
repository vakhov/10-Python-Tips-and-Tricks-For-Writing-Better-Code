# Unpacking

# Normal
items = (1, 2)

print(items)

# Unpacking
a, b = (1, 2)

print(a)
print(b)

# #######################################

# Unpacking
a, _ = (1, 2)
print(a)

# #######################################

a, *b, c = (1, 2, 3, 4, 5)

print(a)
print(b)
print(c)

# #######################################
a, b, *_, d = (1, 2, 3, 4, 5, 6, 7,)

print(a)
print(b)
print(d)

# #######################################
