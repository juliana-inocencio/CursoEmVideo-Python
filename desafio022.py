nome = str(input('Qual o seu nome? ' )).strip()
print(f'O seu nome em letras minusculas é {nome.lower()}')
print(f'O seu nome em letras maiusculas é {nome.upper()}')
espaco = (nome.count(' '))
letras = (len(nome))
nome1 = nome.split()[0]
print(f'O seu nome tem {letras - espaco} letras e seu primeiro nome {len(nome1)}')


