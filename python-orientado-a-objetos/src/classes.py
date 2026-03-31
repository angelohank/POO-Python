class Televisao():
    def __init__(self, marca, valor, nr_canais, ano_lancamento):
        self.marca = marca
        self.valor = valor
        self.nr_canais = nr_canais
        self.ano_lancamento = ano_lancamento

# criando instancia de uma nova televisao
# separando um espaço na memória para ela
tv_1 = Televisao()

# isso terá uma saida parecida com: <__main__.Televisao object at 0x00000182A03CFCD0>
# mostrando em que endereço da memória a minha nova variavel, do tipo Televisao, está armazenada
print(tv_1)


#removendo referenciacao de objetos
tv_1 = None