# Zip

names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Barman']

for index, name in enumerate(names):
    hero = heroes[index]
    print(f'{name} is actually {hero}')

# #######################################

for name, hero in zip(names, heroes):
    print(f'{name} is actually {hero}')

# #######################################

universes = ['Marvel', 'DC', 'Marvel', 'DC']

for name, hero, universe in zip(names, heroes, universes):
    print(f'{name} is actually {hero} from {universe}')

# #######################################

for values in zip(names, heroes, universes):
    print(values)
