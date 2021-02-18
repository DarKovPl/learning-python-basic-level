tax = (4, 7, 8, 23)

print(tax[2])
print('-----')
print(tax[-1])
print('-----')
print(tax.index(7))
print('-----')
print(tax.count(8))
print('-----')
print(max(tax))
print('-----')
taxList = list(tax)
print(taxList)
print('-----')
taxList.append(30)
print(taxList)
print('-----')
newTax = tuple(taxList)
print(newTax)

print('-----')
(tax1, tax2, tax3, tax4) = tax  #  Można przypisywać za jednym razem
                                # wiele zmiennych z tuple. tax to tupla z początku pliku która
                                # została rozbita na wiele zmiennych z tej tupli
print(tax1, tax2, tax3, tax4)
print('-----')

a = 1
b = 10
print('a=', a, 'b=', b)

(a, b) = (b, a)
print('a=', a, 'b=', b)

print(*tax)

# Laboratory

marketing = ['loyalty program', 'client promotion',
             'market research']
print(marketing)
marketing.append('public relations')
print(marketing)
print(marketing[3])
marketing.insert(2, 'investor relations')
print(marketing)
emailMarketing = marketing.copy()
emailMarketing.sort()
print(emailMarketing)
internalEmails = ['internal communication']
emailMarketing.extend(internalEmails)
print(emailMarketing)

emailMarketingTuple = tuple(emailMarketing)
print(emailMarketingTuple)
