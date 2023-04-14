n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2
print(f'A sua média foi {media:.1f}')
print(f'PARABÉNS' if media>=6 else 'ESTUDE MAIS')