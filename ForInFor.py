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

list_noun = ['dog', 'potato', 'meal', 'ice cream', 'car']
list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']

for noun in range(len(list_noun)):

    for adj in range(len(list_adj)):
        print(list_adj[adj], list_noun[noun])
