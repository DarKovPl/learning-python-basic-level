countryLeaders = {'PL': 'Duda', 'US': 'Trump'}
print(countryLeaders['US'])

countryLeaders['DE'] = 'Merkel'
print(countryLeaders)

print('--------------------------------------')
print(countryLeaders.keys())
print(countryLeaders.values())
print(countryLeaders.items())
print('--------------------------------------')
# print(countryLeaders.popitem())  # Destruktywna
# iteracja po słowniku
print(countryLeaders)
print('--------------------------------------')
print(countryLeaders.setdefault('FR', 'Macron'))  # Dodaje do sławnika podaną
# wartość jeśli nie ma jej w słowniku
print(countryLeaders)
print('--------------------------------------')
print(countryLeaders.get('RU'))
print('--------------------------------------')
print(countryLeaders)
newLeaders = {'RU': 'Putin', 'DE': 'Shultz'}
print(newLeaders)
countryLeaders.update(newLeaders)  # Update zastępuje nową wartością w starym
# słowniku jesli nowy słownik posiada w sobie zdublowaną wartość

print(countryLeaders)
print('--------------------------------------')
# Laboratory
chanels = {'Google': 1480, 'Email': 300,
           'Natural Traffic': 400, 'Tv Spot': 700}
print(chanels['Email'])
chanelsUpdate = {'Natural Traffic': 520, 'News': 600}
print(chanelsUpdate)
chanels.update(chanelsUpdate)
print(chanels)
print(chanels.keys())
chanels.pop('Email')
print(chanels)
