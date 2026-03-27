# Televisoes

# TV 1
ano_lancamento = 2025
marca = 'LG'
preco = 1200.00
nr_canais = 30

# TV 2
ano_lancamento = 2026
marca = 'Samsunb'
preco = 1500.00
nr_canais = 50

# Para cada TV que for criada, é necessário copiar e colar o código, sendo que elas tem as mesmas caracteristicas

# mesmo usando um dicionario, a copia de código existe conforme a necessidade de criar novas televisoes
tv_3 = {'ano_lancamento': 2024, 'preco': 1200.00, 'nr_canais': 30, 'marca': 'AOC'}

def criar_tv(ano_lancamento, marca, preco, nr_canais):
    #cria um objeto do tipo TELEVISAO
    tv = {'ano_lancamento': ano_lancamento, 'preco': preco, 'nr_canais': nr_canais, 'marca': marca}

    return tv

# para criar, basta chamar a funcao e passar os valores desejados
# com isso a copia de código é reduzida