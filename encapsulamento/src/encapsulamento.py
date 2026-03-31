class Televisao():
    def __init__(self, nr_canais):
        self.nr_canais = nr_canais

        # dois underscores torna o atributo privado
        # porem, nao impede de chamar direto com o nome igual o declarado
        # Python evita acesso acidental, não impede acesso intencional
        self.__ligada = False

    def aumentar_canais(self, qt_canais):
        self.nr_canais += qt_canais

    def diminuir_canais(self, qt_canais):
        self.nr_canais -= qt_canais

    def ligar(self):
        self.__ligada = True

    # criando metodo privado
    def __metodo_privado(self):
        print('Metodo Privado')

tv = Televisao(3)
print(tv._Televisao__ligada)


# acessando o atributo privado
# isso nao deve ser feito, mas eh possivel
tv._Televisao__ligada = True
print(tv._Televisao__ligada)