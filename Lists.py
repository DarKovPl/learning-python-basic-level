countries = ['FR', 'US', 'DE', 'RU']
print(countries)
print(countries[1])

countries[1] = 'GB'
print(countries)

countries.append('PL')
print(countries)

countries.insert(2, 'ES')
print(countries)

countries.remove('RU')
print(countries)

countries.sort()
print(countries)

countries.reverse()
print(countries)

print(countries.pop(2))  # Kolejka; pobiera elementy
# z listy do przetworzenia i je usuwa z niej.
print(countries)

print(countries.index('PL'))  # Odnajduje element i
# wypluwa numer pozycji w liscie tego elementu

print(countries.count('DE'))  # Liczy ilość podanych
# elementów w liscie

newList = ['FI', 'SE']
countries.extend(newList)  # Rozszerza starą liste o
# nowe argumęty z nowej listy
print(countries)

countriesCopy = countries.copy()  # Tworzy kopie starej
# listy w nowej zmiennej nadając jej nowe miejsce w pamięci
countriesCopy.clear()
print(countries)
print(countriesCopy)

# Laboratory

hitsTitle = ['BROTHERS IN ARMS;', 'BOHEMIAN RHAPSODY;', 'STAIRWAY TO HEAVEN;',
             'RIDERS ON THE STORM;', 'WISH YOU WERE HERE;']
print(*hitsTitle[:3], '\n', *hitsTitle[3:],
      'Total songs:', len(hitsTitle))

print('-----------------------------------------------------------')
hitsTitle.append('CHILD IN TIME;')
hitsTitle.append('AGAIN;')
print(*hitsTitle[:3], '\n', *hitsTitle[3:],
      'Total songs:', len(hitsTitle))

print('----------------------------------------------------------')
hitsTitle.insert(3, 'HOTEL CALIFORNIA;')
print(*hitsTitle[:3], '\n', *hitsTitle[3:6],
      '\n', *hitsTitle[6:], 'Total songs:',  len(hitsTitle))

print('----------------------------------------------------------')
hitsTitle.insert(0, 'THE SOUND OF SILENCE;')
print(*hitsTitle[:3], '\n', *hitsTitle[3:6], '\n',
      *hitsTitle[6:], 'Total songs:', len(hitsTitle))

print('----------------------------------------------------------')
print(hitsTitle.index('HOTEL CALIFORNIA;'))

print('----------------------------------------------------------')
hitsTitle.remove('HOTEL CALIFORNIA;')
print(*hitsTitle[:3], '\n', *hitsTitle[3:6], '\n',
      *hitsTitle[6:], 'Total songs:', len(hitsTitle))

print('----------------------------------------------------------')
hitsTitle.remove('THE SOUND OF SILENCE;')
hitsTitle.insert(0, 'ENJOY THE SILENCE;')
print(*hitsTitle[:3], '\n', *hitsTitle[3:6], '\n',
      *hitsTitle[6:], 'Total songs:', len(hitsTitle))

print('----------------------------------------------------------')
hitsToRead = hitsTitle.copy()
hitsToRead.reverse()
print(*hitsToRead[:3], '\n', *hitsToRead[3:6], '\n',
      *hitsToRead[6:], 'Total songs:', len(hitsToRead))

print('----------------------------------------------------------')
hitsToRead.sort()
print(*hitsToRead[:3], '\n', *hitsToRead[3:6], '\n',
      *hitsToRead[6:], 'Total songs:', len(hitsToRead))

print('----------------------------------------------------------')
hitsToRead.pop(0)
hitsToRead.pop(0)
print(*hitsToRead[:3], '\n', *hitsToRead[3:6], '\n',
      *hitsToRead[6:], 'Total songs:', len(hitsToRead))

print('----------------------------------------------------------')
additionalSongs = [ 'NOTHING COMPARES 2 U;', 'WISH YOU WERE HERE;']
hitsToRead.extend(additionalSongs)
print(*hitsToRead[:3], '\n', *hitsToRead[3:6], '\n',
      *hitsToRead[6:], 'Total songs:', len(hitsToRead))

print('----------------------------------------------------------')
print(hitsToRead.count('WISH YOU WERE HERE;'))
print(hitsToRead.count('RIDERS ON THE STORM;'))

print('----------------------------------------------------------')
hitsToRead.clear()
print(hitsToRead)
