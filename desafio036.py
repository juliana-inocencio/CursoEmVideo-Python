valordacasa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o seu salário? R$ '))
anos = int(input('Em quantos anos você vai pagar? '))
prestacao = valordacasa / (anos*12)
print(f'Para pagar uma casa de R$ {valordacasa:.2f} em {anos} anos, a prestação será de R$ {prestacao:.2f}')
if prestacao > 0.30*salario:
    print('Seu emprestimo foi negado, pois a parcela da casa excede 30% do seu salário.')
else:
    print('Seu emprestimo foi aprovado!')