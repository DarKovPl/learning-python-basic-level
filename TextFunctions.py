import string

line = 'this IS a very STRANGE text'

print(line.capitalize())  # Pierwsza litera w zdaniu duża, reszta małe

print(line.title())  # Każda pierwsza litera każdego wyrazu duża

print(line.upper())

print(line.lower())

print(line.swapcase())  # Zamiana dużych liter na małe i małych na duże litery
print('-----------------------------------------------------')

print('Number: 2')
print(line.casefold())  # Zamiana znaków "agresywna" na małe oraz niektóre narodowe na "normalne".

line = 'der Fluß'
print(line.lower())
print(line.casefold())
print('-----------------------------------------------------')

print('Number: 3')
line = 'ŻÓŁĆ'
print(line.lower())
print(line.casefold())
print(line.replace('Ż', 'Z').replace('Ó', 'O').replace('Ł', 'L')
      .replace('Ć', 'C').lower())
print('-----------------------------------------------------')

print('Number: 4')
line = 'this IS a very STRANGE text'

print(line.count('e'))
print(line.find('e'))
print(line.rfind('e'))  # Funkcja znajdowania znaku od prawej strony
print(line.index('e'))
print(line.rindex('e'))
print('-----------------------------------------------------')

print('Number: 5')
print(line.find('p'))  # Różnica pomiędzy index a find: find jak nie znajdzie szukanego znaku
                       # to zwraca wartość -1 a index error.
print('-----------------------------------------------------')

print('Number: 6')
print('e' in line)
print('p' in line)
print('-----------------------------------------------------')

print('Number: 7')
print(line.startswith('this'))  # Sprawdzenie czy text zaczyna się określonym znakiem
print(line.startswith('THIS'))
print('-----------------------------------------------------')

print('Number: 8')
print(line.endswith('text'))  # Sprwadzenie czy text kończy się określonym znakiem
print('-----------------------------------------------------')

print('Number: 9')
line = """this is a long text
that spans multiple lines
but should be somehow presented in python"""

print(line)
print('-----------------------------------------------------')

print('Number: 10')
print(string.ascii_letters)

print(string.digits)
print('-----------------------------------------------------')

line = 'this is the end of this lesson'
print(line.split(' '))

list = line.split(' ')
print(list)

print(' '.join(list))

# Laboratory

