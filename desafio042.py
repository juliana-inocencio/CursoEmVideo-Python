reta1 = float(input('Primeira reta '))
reta2 = float(input('Segunda reta '))
reta3 = float(input('Terceira reta '))
if (reta2-reta3) <reta1<reta2+reta3:
    if reta1 == reta2 ==reta3:
        print('Os seguimentos acima podem formar um triângulo equilátero')
    elif reta1 == reta2 or reta1 == reta3  or reta2 == reta3:
        print('Os seguimentos acima podem formar um triângulo isósceles')
    elif reta1 != reta2 != reta3:
        print('Os seguimentos acima podem formar um triângulo escaleno')
else:
    print('Não pode formar um triangulo')