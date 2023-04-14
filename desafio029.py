v = float(input('Qual a velocidade do carro? '))
if v > 80:
    print(f'Você foi multado. A multa é de R$ {(v-80)*7:.2f}')
else:
    print('Parabéns por andar dentro da velocidade. Segurança salva vidas!')