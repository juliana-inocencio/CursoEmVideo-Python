distancia = float(input('Qual a distância da sua viagem em km? '))
if distancia <= 200:
    print(f'O preço da passagem é de R$ {distancia*0.50:.2f}')
else:
    print(f'O preço da passagem é de R${distancia*0.45:.2f}')

# preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
# print(f'E o preço da sua passagem será de R$ {preço:.2f})