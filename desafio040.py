nota1 = float(input('Digite a nota: '))
nota2 = float(input('Digite a nota: '))
media = (nota1+nota2)/2
print(f'A media do aluno é {media}')
if media < 5:
    print('Reprovado')
elif media >= 7:
    print('Aprovado')
elif media >=5 and media <= 6.9:
    print('Recuperação')
