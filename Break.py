for candidate in range(2, 31):

    isPrime = True

    for divider in range(2, candidate):

        if candidate % divider == 0:
            isPrime = False
            print('%2d is not a prime number - divider is %2d '
                  % (candidate, divider))
            break
    if isPrime:
        print('%2d is prime!' % candidate)
print('-----------------------------------------------------------')

for candidate in range(2, 31):

    for divider in range(2, candidate):

        if candidate % divider == 0:
            print('%2d is not a prime number - divider is %2d '
                  % (candidate, divider))
            break
    else:
        print('%2d is prime!' % candidate)
print('-----------------------------------------------------------')

text = '''Mechanical advantage is a measure of the force amplification 
achieved by using a tool, mechanical device or machine system. The 
device preserves the input power and simply trades off forces against 
movement to obtain a desired amplification in the output force. The 
model for this is the law of the lever. Machine components designed 
to manage forces and movement in this way are called mechanisms.[1] 
An ideal mechanism transmits power without adding to or subtracting 
from it. This means the ideal mechanism does not include a power 
source, is frictionless, and is constructed from rigid bodies that 
do not deflect or wear. The performance of a real system relative 
to this ideal.'''.split(' ')

counter = 0
short_text = " "

for word in text:

    short_text += word + ' '
    counter += 1

    if counter >= 20:
        print('Short definition of the article: ' + short_text)
        break
print('-----------------------------------------------------------')

definitions = [
    'Mechanical advantage is a measure of the force amplification achieved by using a tool, mechanical device or '
    'machine system. The device preserves the input power and simply trades off forces against movement to obtain a '
    'desired amplification in the output force. The model for this is the law of the lever. Machine components '
    'designed to manage forces and movement in this way are called mechanisms.[1] An ideal mechanism transmits power '
    'without adding to or subtracting from it. This means the ideal mechanism does not include a power source, '
    'is frictionless, and is constructed from rigid bodies that do not deflect or wear. The performance of a real '
    'system relative to this ideal.',
    'Ein Kraftwandler ist eine mechanische Anordnung zur Veränderung einer Kraft in Bezug auf ihren Angriffspunkt, '
    'ihre Richtung oder ihren Betrag. Die einfachsten Kraftwandler sind Seile, Stangen, Rollen, schiefe Ebenen und '
    'Hebel. Dies sind gleichzeitig die grundlegenden einfachen Maschinen.',
    'La ventaja mecánica es una magnitud adimensional que indica cuánto se amplifica la fuerza aplicada usando un '
    'mecanismo (ya sea una máquina simple, una herramienta o un dispositivo mecánico más complejo) para contrarrestar '
    'una carga de resistencia.',
    'Cette notion s\'applique de manière évidente dans les systèmes de poulies et de leviers. Elle est centrale dans '
    'les systèmes de freinage : on applique une petite force sur un parcours important et l\'on obtient une force '
    'importante transmise au système de freinage pour une course de faible distance.'
]

appendOneDefinition = []
dividedOneDefinition = ''
outputList = []

for oneDef in definitions:

    appendOneDefinition.append(oneDef)

    for toOneString in appendOneDefinition:

        dividedOneDefinition = toOneString.split(' ')

        for appendDefToList in dividedOneDefinition:

            outputList.append(appendDefToList)

            if len(outputList) == 20:
                print(*outputList)
                outputList.clear()
                dividedOneDefinition.clear()
                appendOneDefinition.clear()  # Ostatni kod na dole to samo co to tylko poprawione. Nie wiem, dlaczego to tak napisałem jakiś niedorozwój umysłowy chyba.
print('-----------------------------------------------------------')

for definition in definitions:

    words = definition.split(' ')
    short_text = ''
    counter = 0

    for word in words:

        short_text += word + ' '
        counter += 1

        if counter >= 20:
            print(short_text)
            break

print('-----------------------------------------------------------')

dividedOneDefinition = ''
outputList = []

for oneDef in definitions:

    dividedOneDefinition = oneDef.split(' ')

    for appendDefToList in dividedOneDefinition:

        outputList.append(appendDefToList)

        if len(outputList) == 20:

            print(*outputList)
            outputList.clear()
            dividedOneDefinition.clear()
            appendOneDefinition.clear()
