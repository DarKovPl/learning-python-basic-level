itRains = False

if itRains:
    print('We stay at home')
else:
    print('We go out')

print('We stay at home' if itRains else 'We go out')

# Laboratory
musclePain = False
fever = False
weakness = True
isMan = False

print('Suspicion of influenza' if musclePain and fever and weakness
      else 'The flu is unlikely')
print('-------------------------------------------------------------')
if musclePain and fever and weakness:
    print('Suspicion of influenza')
elif weakness and not (fever and musclePain):
    print('Just take a rest')
elif musclePain or fever:
    print('You may be cold')
else:
    print('You are healthy')
print('--------------------------------------------------------------')
if isMan and (musclePain or fever or weakness):
    print('Suspicion of influenza')
elif not isMan and weakness and not (musclePain and fever):
    print('Just take a rest')
elif not isMan and fever or musclePain:
    print('You may be cold')
else:
    print('You are healthy')
print('---------------------------------------------------------------')
isCheckCompleted = False
print('Check is completed' if isCheckCompleted else 'Check not done yet')
