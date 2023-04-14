a = float(input('Qual o comprimento do cateto oposto? '))
b = float(input('Qual o comprimento do cateto adjacente? '))
c = ((a**2)+(b**2))**(1/2)
# ou dessa forma h = c**(1/2)
print(f'O comprimento da hipotenusa é {c:.2f}')


