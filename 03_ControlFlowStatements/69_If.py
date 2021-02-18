age = 19

if age >= 18:
    print('You are adult and you can buy alcohol')
else:
    print('You are too young to buy alcohol')

isDrunk = False
if age >= 18 and not isDrunk:
    print('You are adult and you can buy alcohol')
else:
    print('Sorry, we cannot sell you alcohol')

isRestrictedArea = False
if age >= 18 and not isDrunk and not isRestrictedArea:
    print('You are adult and you can buy alcohol')
else:
    print('Sorry, we cannot sell you alcohol')
print('--------------------------------------------')
#  Laboratory
like = 600
share = 500
if like > 500 and share > 100:
    print('We got {0:d} likes and {1:d} shares. '
          'Prices are lower now by 10%'.format(like, share))
else:
    print('Sorry, we got only {0:d} likes, '
          'and {1:d} shares.\nIs missing {2:d} '
          'likes and {3:d} shares'.format(like, share,
                                          500 - like, 100 - share))
print('---------------------------------------------------')
isPizzaOrdered = True
isWorkDays = True
isBigSoftDrinkOrdered = False

if isWorkDays and isPizzaOrdered and isBigSoftDrinkOrdered:
    print('Congratulations you won a ticket on free Burger')
else:
    print('You won nothing. Please buy more.')
print('---------------------------------------------------')
fileSize = 47
diskSize = 70
diskUsed = 23

if fileSize < diskSize - diskUsed:
    print('You have enough free space on your'
          ' Hard Drive to download this file')
else:
    print("You don't have enough free space on your"
          " Hard Drive to download this file")