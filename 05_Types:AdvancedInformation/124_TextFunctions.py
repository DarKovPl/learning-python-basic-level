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

list1 = line.split(' ')
print(list1)

print(' '.join(list1))
print('-----------------------------------------------------')

# Laboratory

poem = '''1.Runą i w łunach spłoną pożarnych 
Krzyże kościołów, krzyże ofiarne 
I w bezpowrotnym zgubi się szlaku 
W lechickiej ziemi Orzeł Polaków. 
2.O, jasne słońce- wodzu Stalinie! 
Niech sława twoja nigdy nie zginie 
Niechaj jak orły powiedzie z gniazda 
Rosja i z Kremla płonąca gwiazda. 
3.Na ziemskim globie flagi czerwone 
Będą na wiatrach grały jak dzwony 
Czerwona Armia i wódz jej Stalin 
Odwiecznych wrogów na zawsze obali! 
4.Zaćmisz się rychło w czarnej godzinie 
Polsko- Twe córy i syny, 
Wiara i każdy krzyż na mogile, 
U stóp am legą w prochu i pyle! '''.split('\n')

lines = poem

for each_line in range(8):

    print(lines[each_line])
    print(lines[each_line+8])
