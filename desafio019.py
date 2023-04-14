import random
aluno1 = str(input('Digite o nome do aluno: '))
aluno2 = str(input('Digite o nome do aluno: '))
aluno3 = str(input('Digite o nome do aluno: '))
aluno4 = str(input('Digite o nome do aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
sorteio = random.choice(lista)
print(f'O Aluno que vai apagar a lousa é {sorteio}.')

