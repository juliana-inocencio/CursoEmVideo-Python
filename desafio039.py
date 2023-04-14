from datetime import date
ano = int(input('Qual seu ano de nascimento? '))
idade = date.today().year-ano
print(f'Quem nasceu em {ano} tem {idade} anos em {date.today().year}.')
if idade < 18:
    print(f'Você ainda vai se alistar. Seu alistamento é em {18-idade} anos.')
elif idade == 18:
    print('Está na hora de se alistar. Procure o posto militar mais próximo.')
elif idade > 18:
    print(f'Você deveria ter se alistado há {idade-18} ano(s).')
