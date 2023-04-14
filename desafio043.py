peso = float(input('Qual o seu peso em kg? '))
altura = float(input('Qual a sua altura em metros? '))
imc = peso/altura**2
print(f'Seu IMC é {imc:.1f}')
if imc < 18.5:
    print('Abaixo do Peso')
elif imc >= 18.5 and imc <= 25:
    print('Peso ideal')
elif imc >25 and imc <= 30:
    print('Sobrepeso')
elif imc >30 and imc <40:
    print('Obesidade')
elif imc >40:
    print('Obesidade mórbida')