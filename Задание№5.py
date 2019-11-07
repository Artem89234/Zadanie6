a = int (input('A:'))
b = int (input('B:'))
if(a/b):
    o = 0
    o = a % b
    ch = 0
    ch = a / b
    print()
    print('A делятся B')
    print('Остаток=',o)
    print('Частное=',ch)
else:
    print('A не делится B')
if(b/a):
    o = 0
    o = b % a
    ch = 0
    ch = b / a
    print()
    print('Остаток=',o)
    print('Частное=',ch)
    print('B делятся A')
else:
    print('B не делится A')

    
