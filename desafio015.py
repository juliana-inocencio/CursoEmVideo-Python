d = int(input('Quantos dias alugado? '))
km = float(input('Quantos km rodado? '))
final = (60*d) + (0.15*km)
print(f'O total a pagar é de R$ {final:.2f}')
