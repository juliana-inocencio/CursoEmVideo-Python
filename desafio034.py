salario = float(input('Qual o valor do salário? '))
if salario <= 1250:
    print(f'O seu novo salário será de R$ {(salario*0.15)+salario:.2f}')
else:
    print(f'O seu novo salário será de R$ {(salario*0.10)+salario:.2f}')