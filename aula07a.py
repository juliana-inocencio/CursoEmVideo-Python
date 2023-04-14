n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma de {} e {} é {}, o produto é {} e a divisão é {},'.format(n1,n2,s,m,d), end=' bem como a divisão inteira é {} e a potência é {}.'.format(di,e))