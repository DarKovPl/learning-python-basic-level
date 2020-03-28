somethingLikeNumber = '1000'
print(somethingLikeNumber)

intSomethingLikeNumber = int(somethingLikeNumber) + 1
print(intSomethingLikeNumber)

strSomethingLikeNumber = somethingLikeNumber + str(1)
print(strSomethingLikeNumber)

print(type(somethingLikeNumber))
print(type(intSomethingLikeNumber))
print(type(strSomethingLikeNumber))

# Laboratory
article = '''Monty Python (also collectively known as the Pythons)[2][3] were a British surreal comedy group who created
 the sketch comedy television show Monty Python's Flying Circus, which first aired on the BBC in 1969. Forty-five 
 episodes were made over four series. The Python phenomenon developed from the television series into something larger 
 in scope and impact, including touring stage shows, films, numerous albums, several books and musicals. The Pythons' 
 influence on comedy has been compared to the Beatles' influence on music.[4][5][6] Regarded as an enduring icon of 
 1970s pop culture, their sketch show has been referred to as being “an important moment in the evolution of television 
 comedy".[7]'''

print(article.upper())
print("---------------------------------------------------------------")
print(article.lower().replace("monty", "flying"))
print("----------------------------------------------------------------")
print(article.split(" "))
print("----------------------------------------------------------------")
print("World Python appears {} times".format(article.lower().count("python")))
print('----------------------------------------------------------------')
print("To print the \\ you need to put \\ twice in your text. Like this: \\\\")
print('The best of' + " '80s !!!")
print("------------------------------------------------------------------")
amountPLN = 234
horizontalChart = ['\t', 'cur', '\t', 'exchange', '\t', 'amount']
verticalChart = {0: ['\n', '\t', 'USD'], 1: ['\n', '\t', 'EURO']}
currency = {'USD': 3.65, 'EUR': 4.23}

print(*horizontalChart)
print(*verticalChart.get(0), '\t', currency.get('USD'),
      '\t'*2, round(amountPLN / currency.get('USD'), 2),
      *verticalChart.get(1), '\t', currency.get('EUR'),
      '\t'*2, round(amountPLN / currency.get('EUR'), 2))
print('-------------------------------------------------------------------')
valueAsText = '123.45'
factor = 1.23
print('Value is ' + valueAsText + ' factor is ' + str(factor)
      + '. Value * Factor =', float(valueAsText) * factor)
