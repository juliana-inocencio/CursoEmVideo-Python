num = (int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')))

print(num)
print(f'O número 9 apareceu {num.count(9)} vezes')

if 3 in num:
     print(f'O número 3 aparece na posição {num.index(3)+1}')
else:
     print('O número 3 não apareceu nenhuma vez')
for c in num:
    if c %2 ==0:
        print(f'Os números pares são {c}')

