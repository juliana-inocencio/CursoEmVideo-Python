print('Conversor de bases númericas')
num = int(input('Digite um número: '))
num2 = int(input('''Escolha uma das bases:
[1] para binário
[2] para octal
[3] para hexadecimal
Opção: '''))
if num2 == 1:
    print(f'O {num} convetido para binário é {bin(num)}')
elif num2 == 2:
    print(f'O {num} convetido para octal é {(oct(num))}')
elif num2 == 3:
    print(f'O {num} convetido para hexadecimal é {(hex(num))}')