isWeekend = True
print("Is weekend =", isWeekend)

temperature = 25
print('Temperature =', temperature)

toDoList = ''
print('To do list =', toDoList)

isHappy = isWeekend and temperature >= 20 and toDoList == ''
print('Is Happy =', isHappy)

isHappy = not isWeekend and temperature < 20 and toDoList != ''
print('Is Happy =', isHappy)

isHappy = isWeekend and temperature >= 20 and toDoList == '' \
          or not isWeekend and temperature < 20 and toDoList != ''
print('Is Happy =', isHappy)

# Laboratory

isAutomaticMode = False
is80PercentLight = True
isDirectLight = False
isRainy = False
turnLightsOn = (isAutomaticMode and (not is80PercentLight
                or isDirectLight or isRainy))
print('Automatic mode: ', isAutomaticMode)
print('Is the light good: ', is80PercentLight)
print('Is Sun low: ', isDirectLight)
print('Is it rainy: ', isRainy)
print('Turn Lights On: ', turnLightsOn)
