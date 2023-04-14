import math
a = float(input('Qual o comprimento do cateto oposto? '))
b = float(input('Qual o comprimento do cateto adjacente? '))
hi = math.hypot(a,b)
print(f'A hipotenusa vai medir {hi:.2f}')

