import random

print('One random number:', random.randint(1, 100), '\n')  # Losujemy liczbe całkowitą od 1 do 100

print('Choosing random number from a range', random.choice(range(1, 100)),
      '\n')  # Losujemy jeden element z podanego zasięgu.

print('Choosing random number from a range - easier', random.randrange(1, 100),
      '\n')  # Robi dokładnie to samo co powyżej.

list = ['John', 'Ann', 'Peter', 'Susan', 'Emily', 'Greg', 'Chris']
random.shuffle(list)
print('Recorded list:', list, '\n')

print('Just a random float', random.random())
print('-----------------------------------------------------')

# Laboratory

for num in range(10):
    random_number = random.randint(1, 100)
    print('{0:d} - random number: {1:d}'.format(
        num + 1, random_number))
print('-----------------------------------------------------')

number_to_find = random.randint(1, 100)
counter = 0
print('We are searching this number: %d' % number_to_find)

while True:

    number_1 = random.randint(1, 100)
    counter += 1

    if number_1 == number_to_find:
        print("I'm found the correct number: %d" % number_1)
        print('But I needed for this %d loops' % counter)
        break
print('-----------------------------------------------------')

countries = ['Uruguay', 'Russia', 'Saudi Arabia', 'Egypt',
             'Spain', 'Portugal', 'Iran', 'Morocco',
             'France', 'Denmark', 'Peru', 'Australia',
             'Croatia', 'Argentina', 'Nigeria', 'Iceland',
             'Brazil', 'Switzerland', 'Serbia', 'Costa Rica',
             'Sweden', 'Mexico', 'Korea Republic', 'Germany',
             'Belgium', 'England', 'Tunisia', 'Panama',
             'Colombia', 'Japan', 'Senegal', 'Poland'
             ]
random.shuffle(countries)
group_number = 0
print(len(countries))
for nam_countries in range(len(countries)):

    if nam_countries % 4 == 0:

        group_number += 1
        print("---Group %d---" % group_number)

    print(countries[nam_countries])
