age = 21
isDrunk = False
isRestrictedArea = False

if age < 18:
    print('You are too young to buy alcohol')
else:
    if isDrunk:
        print("Are you drunk? Sorry, I can't sell you alcohol")
    else:
        if isRestrictedArea:
            print('Restricted area. Alcohol is forbidden')
        else:
            print('Okay, you can buy alcohol')
print('---------------------------------------------------------')
if age < 18:
    print('You are too young to buy alcohol')
elif isDrunk:
    print("Are you drunk? Sorry, I can't sell you alcohol")
elif isRestrictedArea:
    print('Restricted area. Alcohol is forbidden')
else:
    print('Okay, you can buy alcohol')

#  Laboratory  <<<<< do zrobienia
shares = 101
likes = 500

if likes >= 501 and shares >= 101:
    print('Likes are {0:d}. Shares are {1:d}. We have for '
          'you special offer as 10 percent discount.'
          .format(likes, shares))
else:
    if likes <= 499 and shares <= 99:
        print('Special offer starts when shares cross 99 and'
              ' likes will be above 499. Currently likes: {0:d} '
              'and shares: {1:d}')
    else:
        if likes == 500:
            print('Likes are exactly 500 and we start '
                  'with 10 % discount if shares cross 100')
        else:
            if shares == 100:
                print('Shares are exactly 100 and we will sell'
                      ' everything with 10% off but likes must across'
                      ' 499 too')