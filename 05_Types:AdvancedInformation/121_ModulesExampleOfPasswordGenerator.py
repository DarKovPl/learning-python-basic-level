import random

for i in range(32, 127):
    print(i, chr(i))  # Tabela ASCII. Tabela posiada 256 znaków.
print('-----------------------------------------------------')

ints = range(33, 127)
password = ''

for i in range(16):
    password += chr(random.choice(ints))
print('Password is: ', password)
print('-----------------------------------------------------')

# Laboratory

min_variable = 1
max_variable = 7
dice = random.choice(range(min_variable, max_variable))

if dice == 1:
    print(dice, ":\n\n  o\n")

elif dice == 2:
    print(dice, ":\n\to\n\no")

elif dice == 3:
    print(dice, ":\n\to\n  o\no")

elif dice == 4:
    print(dice, ":\no\to\n\no\to")

elif dice == 5:
    print(dice, ":\no\to\n  o\no\to")

else:
    print(dice, ':', "\no\to\to"*2)
print('-----------------------------------------------------')

list_of_five_throws_of_dice = []

for throws in range(5):

    list_of_five_throws_of_dice.append(random.choice(range(min_variable, max_variable)))

list_of_five_throws_of_dice.sort()
print(*list_of_five_throws_of_dice)
