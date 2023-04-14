import math
num = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(num))
cos = math.cos(math.radians(num))
tan = math.tan(math.radians(num))
print(f'O cosseno de {num} é {cos:.2f}')
print(f'A tangente de {num}  é {tan:.2f}')
print(f'E o seno de {num}  é {seno:.2f}')


