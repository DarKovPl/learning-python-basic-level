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

#  Laboratory  <<<<< to do
print('Laboratory-----------------------------------------------')
shares = 100
likes = 500

if likes >= 500 and shares >= 100:
    print('Likes are {0:d}, and shares are {1:d}. W start selling'
          ' everything 10% cheaper'.format(likes, shares))
else:
    if likes < 500 and shares >= 100:
        print('Likes are {0:d}. There are too low likes, but'
              ' shares are {1:d}, and there are enough.'
              .format(likes, shares))
    else:
        if likes >= 500 and shares < 100:
            print('Shares are {0:d}. There are too low shares, but'
                  ' likes are {1:d}, and there are enough.'
                  .format(shares, likes))
        else:
            print('Likes are {0:d}, and shares are {1:d}, and'
                  ' these are too low to start promotion.'
                  .format(likes, shares))
print('----------------------------------------------------------')
if likes >= 500 and shares >= 100:
    print('Likes are {0:d}, and shares are {1:d}. W start selling'
          ' everything 10% cheaper'.format(likes, shares))
elif likes < 500 and shares >= 100:
    print('Likes are {0:d}. There are too low likes, but'
          ' shares are {1:d}, and there are enough.'
          .format(likes, shares))
elif likes >= 500 and shares < 100:
    print('Shares are {0:d}. There are too low shares, but'
          ' likes are {1:d}, and there are enough.'
          .format(shares, likes))
else:
    print('Likes are {0:d}, and shares are {1:d}, and'
          ' these are too low to start promotion.'
          .format(likes, shares))
print('----------------------------------------------------------')
ifPizza = False
pizza = 'Pizza'

ifBigSoftDrink = False
bigDrink = 'Big Soft Drink'

notWeekendDay = False
dayOfTheWeek = 'weekday'

reward = 'Burger'

if (ifPizza or ifBigSoftDrink) and notWeekendDay:
    print('You have from us one coupon for free %s' % reward)
else:
    if (not ifPizza or not ifBigSoftDrink) and notWeekendDay:
        print("You don't have ordered %s or %s. Order something to get"
              " a ticket for free %s" % (pizza, bigDrink, reward))
    else:
        if (ifPizza or ifBigSoftDrink) and not notWeekendDay:
            print('Today is not a %s. Today is weekend and '
                  'special offer is not available'
                  % dayOfTheWeek)
        else:
            print('Order {0:s} or {1:s} but on {2:s} to get free {3:s}'
                  .format(pizza, bigDrink, dayOfTheWeek, reward))
print('-------------------------------------------------------------')

if (ifPizza or ifBigSoftDrink) and notWeekendDay:
    print('You have from us one coupon for free %s' % reward)
elif (not ifPizza or not ifBigSoftDrink) and notWeekendDay:
    print("You don't have ordered %s or %s. Order something to get"
          " a ticket for free %s" % (pizza, bigDrink, reward))
elif (ifPizza or ifBigSoftDrink) and not notWeekendDay:
    print('Today is not a %s. Today is weekend and '
          'special offer is not available'
          % dayOfTheWeek)
else:
    print('Order {0:s} or {1:s} but on {2:s} to get free {3:s}'
          .format(pizza, bigDrink, dayOfTheWeek, reward))
