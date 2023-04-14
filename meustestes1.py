valor = float(input())
quantidade = int(input())

valortotal = valor * quantidade

desconto1 = valortotal*0.1

desconto2 = (0.01*valortotal)*quantidade

descontototal = desconto1 + desconto2

print(f'{valortotal:.2f}')
print(f'{valortotal-descontototal:.2f}')