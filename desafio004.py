n = input('Digite algo: ')
print('O tipo primitivo desse valor é {}.'.format(type(n)))
print('É um número?' ,(n.isnumeric()))
print('É alfabético?' ,(n.isalpha()))
print('É alfanumérico?' ,(n.isalnum()))
print('Está em maiúscula?' ,(n.isupper()))
print('Está em minúscula?' ,(n.islower()))

