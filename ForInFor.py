for x in range(1, 11):
    line = str(x)
    for y in range(1, 11):
        line += ('\t%3d' % (x * y))
    print(line)
print('-----------------------------------------------------------')

i = 10
factorial = 1

for f in range(i):
    factorial = (f + 1) * factorial
    print('{0:1d}!\t= {1:7d}'.format(f + 1, factorial))
print('-----------------------------------------------------------')

i = 11
textListFactorial = []
z = textListAddNumbersForMultiple = []
characters = ['{}']

for f in range(i):

    factorial = 1
    textListFactorial.append(f)

    for f2 in range(f):

        factorial *= (f2 + 1)
        textListAddNumbersForMultiple.append(f2+1)

        print(f, f2 + 1, factorial)

    print('{0:2d}!\t= '.format(textListFactorial.pop(0), ))
print(textListAddNumbersForMultiple)

list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']
