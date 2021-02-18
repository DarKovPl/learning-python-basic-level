i = 1
while i <= 10:
    print(i)
    i += 1
else:
    print('Now variable i =', i)
print('---------------------------------------------------------------')
#  Laboratory
firstRow = 1
currentRow = firstRow
lastRow = 31
while currentRow <= lastRow:
    print('Row number: ', currentRow)
    currentRow += 1
print('---------------------------------------------------------------')
number = 1
squareOfTheNumber = 0
cubeOfTheNumber = 0
while number <= 13:
    squareOfTheNumber = number ** 2
    cubeOfTheNumber = number ** 3
    print('Square of the number: {0:d} is '.format(number), squareOfTheNumber,
          '  \t  ', 'and', '\t' * 2, 'Cube of the number: {0:d} is '
          .format(number), cubeOfTheNumber)
    number += 1
print('----------------------------------------------------------------')
iteration = 0
numberToIncrease = 2
while iteration <= 16:
    result = numberToIncrease ** iteration
    print('Exponentiation of 2: ', result)
    iteration += 1
print('---------------------------------------------------------------')
stringX = 'x'
variable = 1
while variable <= 10:
    result = stringX * variable
    print(result)
    variable += 1
