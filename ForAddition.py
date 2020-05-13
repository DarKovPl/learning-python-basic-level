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
dictionaryForIfWordsIsEven = {}
mediatedDictionaryBetweenOddWordsAndFinalOutput = {}
finalOutputDictionary = {}
bootCounterToEliminateTheException = 1
lastKey = 0

for keyOfValue in range(1, len(text)):

    if len(text[keyOfValue]) > 0:

        dictionaryForIfWordsIsEven[keyOfValue] = text[keyOfValue]
        mediatedDictionaryBetweenOddWordsAndFinalOutput[keyOfValue] = dictionaryForIfWordsIsEven[keyOfValue]

        if str(finalOutputDictionary.get(lastKey)) ==\
                str(mediatedDictionaryBetweenOddWordsAndFinalOutput.get(keyOfValue)):

            mediatedDictionaryBetweenOddWordsAndFinalOutput.clear()
            dictionaryForIfWordsIsEven.clear()

            lastKey = list(finalOutputDictionary.keys())[-1]
            bootCounterToEliminateTheException += 1
            continue

        if str(mediatedDictionaryBetweenOddWordsAndFinalOutput.get(keyOfValue)) ==\
                str(dictionaryForIfWordsIsEven.get(keyOfValue - 1)) \
                and bootCounterToEliminateTheException > 1:

            mediatedDictionaryBetweenOddWordsAndFinalOutput.pop(keyOfValue)
            finalOutputDictionary.update(mediatedDictionaryBetweenOddWordsAndFinalOutput)

            dictionaryForIfWordsIsEven.clear()
            mediatedDictionaryBetweenOddWordsAndFinalOutput.clear()

            lastKey = list(finalOutputDictionary.keys())[-1]
            bootCounterToEliminateTheException = 1

    bootCounterToEliminateTheException += 1

else:
    finalOutputDictionary.update(mediatedDictionaryBetweenOddWordsAndFinalOutput)
    dictionaryForIfWordsIsEven.clear()
    mediatedDictionaryBetweenOddWordsAndFinalOutput.clear()

    print('Final output tuple from dictionary with keys and values pairs without repetition elements: ', '\n',
          *finalOutputDictionary.items(), '\n'*2, 'The sum of key-value pairs: ', len(finalOutputDictionary))

