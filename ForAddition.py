fibonacciIterations = 9
sumOfIterations = 0
sumOfIterations2 = 1
sumOfIterations3 = 1

for fibIt in range(fibonacciIterations):

    sumOfIterations = sumOfIterations2 + sumOfIterations3
    sumOfIterations2 = sumOfIterations
    sumOfIterations3 += sumOfIterations2

    print(sumOfIterations3, '  \t  '*2, sumOfIterations2)

