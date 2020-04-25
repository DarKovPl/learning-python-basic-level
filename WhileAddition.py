initialCapital = 20000
percent = 0.03
startTimeYear = 1
summaryPrint = initialCapital

while startTimeYear <= 10:
    initialCapital += initialCapital * percent

    print('Your amount of saved money in {0:2d} year of saving: {1:.2f}'
          .format(startTimeYear, round(initialCapital, 2)))
    startTimeYear += 1

print('Your initial capital amount was %d and your total sum of '
      'interest\nfor ten years saving will be %.2f' %
      (summaryPrint, round(initialCapital - summaryPrint, 2)))
print('-----------------------------------------------------------')

sumOfDigitsInteger = 0
integerString = str(20730906)
listDigitsOfInteger = []

for stringInt in integerString:

    listDigitsOfInteger.append(stringInt)
    sumOfDigitsInteger += int(stringInt)

    if len(listDigitsOfInteger) >= len(integerString):
        print('Digits sum of %s number is %d' % (integerString,
                                                 sumOfDigitsInteger))
print('-----------------------------------------------------------')
