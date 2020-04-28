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

number = 20730906
unchangedNumberToPrint = number
result = 0
niceOutputDigitList = []

while number > 0:

    if number % 10:

        niceOutputDigitList.append(number % 10)
        result += number % 10
        number -= number % 10

    else:

        number = number // 10

print('Digits to addition from number {0:d} are'.format(unchangedNumberToPrint),
      '+'.join([str(digit) for digit in niceOutputDigitList]) +
      '=' + str(result))
print('-----------------------------------------------------------')

text = '''United Space Alliance: This company provides major support to NASA for
various projects, such as the space shuttle. One of its projects is to
create Workflow Automation System (WAS), an application designed to
manage NASA and other third-party projects. The setup uses a central
Oracle database as a repository for information. Python was chosen over
languages such as Java and C++ because it provides dynamic typing and
pseudo-code–like syntax and it has an interpreter. The result is that
the application is developed faster, and unit testing each piece is 
easier.'''.replace('\n', ' ').split(' ')
countingLengthWordsList = []
countedLongWordsList = []
countedShortWordsList = []

while (len(text) or len(countingLengthWordsList)) > 0:

    countingLengthWordsList.extend(text)
    text.clear()

    if len(countingLengthWordsList[0]) > 6:

        countedLongWordsList.append(countingLengthWordsList.pop(0))

    else:

        countedShortWordsList.append(countingLengthWordsList.pop(0))

print('The text has %2d words longer than 6 characters.' % len(countedLongWordsList), '\n',
      'The text has %2d words shorter than 6 characters.' % len(countedShortWordsList))

