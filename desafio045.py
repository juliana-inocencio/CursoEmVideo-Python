from random import randint
print ('-_-.-_-.-_-.-_-.-_-.-_-.-_-.-_-JOKENPÔ-_-.-_-.-_-.-_-.-_-.-_-.-_-.-_-')
pessoa = int(input('''
[1] PEDRA
[2] PAPEL
[3] TESOURA
Qual a sua jogada? '''))
itens = ('Pedra', 'Papel','Tesoura')
computador = randint(0,2)
print(f'O computador jogou {itens[computador]}')
if computador == pessoa:


