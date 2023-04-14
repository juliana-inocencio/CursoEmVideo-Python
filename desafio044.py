print(f'                            =_=_=_=_=_=_= LOJAS INOCENCIO =_=_=_=_=_=_=')
print('')
valor = float(input('VALOR DA COMPRA: R$ '))
print('')
print('----- FORMA DE PAGAMENTO ----- ')
pgto = int(input('''[1] À VISTA - DINHEIRO OU CHEQUE (10% DE DESCONTO)
[2] À VISTA - CARTÃO (5% DE DESCONTO)
[3] EM ATÉ 2x NO CARTÃO - SEM JUROS 
[4] 3x OU MAIS NO CARTÃO - COM JUROS (20% DE JUROS FIXO)
OPÇÃO: '''))
if pgto == 1:
    print(f'''O pagamento da sua compra será à vista no dinheiro/cheque e com 10% de desconto.
Sua compra de R$ {valor:.2f} vai custar R$ {valor-(valor*0.10):.2f}.''')
if pgto == 2:
    print(f'''O pagamento da sua compra será à vista no cartão e com 5% de desconto.
Sua compra de R$ {valor:.2f} vai custar R$ {valor-(valor * 0.05):.2f}.''')
if pgto == 3:
    parcelas1 = input('QUANTAS PARCELAS? ')
    print(f'''O pagamento da sua compra será em até {parcelas1}x no cartão sem juros.
O valor final é de R$ {valor:.2f}''')
if pgto == 4:
    parcelas2 = input('QUANTAS PARCELAS? ')
    print(f'''O pagamento da sua compra será em até {parcelas2}x no cartão com juros.
Sua compra de R$ {valor:.2f} vai custar R$ {valor+(valor * 0.20):.2f}.''')


