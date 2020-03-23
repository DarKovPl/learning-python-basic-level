print("1,2,3")
print(1, 2, 3, sep="-")
print(1, 2, 3, sep="\n")
letterInText = "R"
secondLetterInText = "O"
thirdLetterInText = "M"
print(letterInText, secondLetterInText, thirdLetterInText, sep="\t")
print(letterInText, secondLetterInText, thirdLetterInText, "\a", sep="\t")
print("This is a backslash: \\")
# Backslash i u plus kod asci danego znaku wyświetla go tutaj mamy sigme
print("\u03A3")

# Laboratory

listOfTvPrograms = ['TVP1', 'TVP2', 'TVN', 'Polsat', 'BBC', 'HBO', 'MTV']
print(*listOfTvPrograms[:7], sep=";")
# Powyżej znajduje sie sposób na wyswietlenie listy bez nawiasów. Czyli samej czystej zawartosci listy.

print("I like computers but better is {} but better is {} "
      "but better is {} but better is {} but better is {} "
      "but better is {} but better is {}".format(*listOfTvPrograms))

itemAndTime = {"News", "18:00"}
print("I like watching {} at {} on {}.".format(*itemAndTime,
                                               *listOfTvPrograms[4:]))
