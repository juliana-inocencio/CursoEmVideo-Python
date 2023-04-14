from datetime import date
ano = int(input('Qual o seu ano de nascimento? '))
atual = date.today().year
idade = atual - ano
print(f'Sua idade é {idade} anos.')
if idade <= 9:
    print('Sua categoria é MIRIM')
elif idade <=14:
    print('Sua categoria é INFANTIL')
elif idade <=19:
    print('Sua categoria é JUNIOR')
elif idade ==20:
    print('Sua categoria é SÊNIOR')
elif idade >20:
    print('Sua categoria é MASTER')

