fibonacci = 10
sumOfIterations = 0
sumOfIterations2 = 1
sumOfIterations3 = 1
fibonacciNumbersList = []

for fibIt in range(fibonacci):
    fibonacciNumbersList.append(sumOfIterations2)
    fibonacciNumbersList.append(sumOfIterations3)
    sumOfIterations = sumOfIterations2 + sumOfIterations3
    sumOfIterations2 = sumOfIterations
    sumOfIterations3 += sumOfIterations2

print('Index: ', '\t|| '.join([str(index + 1) for index in
                               range(len(fibonacciNumbersList))]))
print('-------------------------------------------------------------'
      '-------------------------------------------------------------'
      '-----------------------------------------')
print('Number:', '\t|| '.join([str(digit) for digit in
                               fibonacciNumbersList]))
print('-------------------------------------------------------------')

text = """Industrial Light & Magic: In this case, you find Python
used in the production process for scripting complex,
computer graphic-intensive films. Originally, Industrial
Light & Magic relied on Unix shell scripting, but it was
found that this solution just couldn’t do the job. Python
was compared to other languages, such as Tcl and Perl, and
chosen because it’s an easier-to-learn language that the
organization can implement incrementally. In addition, Python
can be embedded within a larger software system as a scripting
language, even if the system is written in a language such as
C/C++. It turns out that Python can successfully interact with
these other languages in situations in which some languages can’t.
""".replace('\n', ' ').split(' ')
counter = 1

for word in text:

    if word.lower().find('p') > -1:
        print(counter, '\t', word)
        counter += 1
print('-------------------------------------------------------------')

dictionary = {'A': '80%-100%', 'B': '60%-80%', 'C': '50-60%',
              'D': 'less then 50%'}
for valueOfDict in dictionary:
    print(valueOfDict, '-', dictionary[valueOfDict])
print('-------------------------------------------------------------')

text.sort()
countingWordsDictionary = {}
countedWordsDictionary = {}
countedWordsDictionary1 = {}
counter = 1
lastKey = 0

for keyOfDicts in range(1, len(text)):

    if len(text[keyOfDicts]) > 0:
        countingWordsDictionary[keyOfDicts] = text[keyOfDicts]
        countedWordsDictionary[keyOfDicts] = countingWordsDictionary[keyOfDicts]

        if str(countedWordsDictionary1.get((lastKey-1))) == str(countedWordsDictionary.get((lastKey+1))) and counter > 1:
            countedWordsDictionary.clear()
            countingWordsDictionary.clear()
            continue
        if str(countedWordsDictionary.get(keyOfDicts)) == str(countingWordsDictionary.get(keyOfDicts - 1)) \
                and counter > 1:
            countedWordsDictionary.pop(keyOfDicts)
            lastKey = keyOfDicts
            countedWordsDictionary1.update(countedWordsDictionary)
            countingWordsDictionary.clear()
            countedWordsDictionary.clear()
            counter = 1

    counter += 1

print(countingWordsDictionary, '\n', countedWordsDictionary, '\n', countedWordsDictionary1)
