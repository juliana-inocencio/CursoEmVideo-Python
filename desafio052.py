num = int(input('Digite o número: '))
tota = 0
for c in range(1, num +1):
    if num % c == 0:
        print('033[33m', end='')
        tot+=1
    else:
        print('033[33m', end='')
    print(f'{c}', end='')
print(f'\n\033[m0)

