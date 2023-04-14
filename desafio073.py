times = ('Palmeiras','Internacional','Fluminense','Corinthians','Flamengo','Athletico-PR','América-MG',
         'Atléico-MG', 'São Paulo', 'Botafogo', 'Fortaleza','Santos','Góias','Bragantino', 'Coritiba',
         'Cuiabá','Atletico-GO','Céara','Avaí','Juventude')
print(f'Os cinco primeiros colocados são: {times[0:5]}')
print(f'Os últimos quatro colocados são: {times[-4:]}')
print(sorted(times))
print(f'O Céara está na posição {times.index("Céara")+1} da tabela')
