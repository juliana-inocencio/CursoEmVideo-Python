pa = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = pa+(10-1)*razao
for c in range (pa,decimo+razao,razao):
    print(c)
