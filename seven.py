# Setattr/Getattr


class Person:
    pass


person = Person()

person.first = 'Walter'
person.last = 'White'

print(person.first)
print(person.last)

# #######################################

person = Person()

first_key = 'first'
first_val = 'Walter'

# person.first_key = first_val
setattr(person, first_key, first_val)
print(person.first)

first = getattr(person, first_key)
print(first)

# #######################################

person = Person()

person_info = {'first': 'Walter', 'last': 'White'}

for key, value in person_info.items():
    setattr(person, key, value)

print(person.first)
print(person.last)


for key in person_info.keys():
    print(getattr(person, key))
