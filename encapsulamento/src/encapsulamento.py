class Televisao():
    def __init__(self, nr_canais):
        self.__ano_lancamento = None
        self.nr_canais = nr_canais
        self.__marca = ""


        # dois underscores torna o atributo privado
        # porem, nao impede de chamar direto com o nome igual o declarado
        # Python evita acesso acidental, não impede acesso intencional
        self.__ligada = False

    # __ano_lancamento = 2000
    @property # o metodo tem que ter o mesmo nome do atributo
    # o decorator basicamente transforma esse metodo, em um atributo, pode ser chamado sem parenteses
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca = marca


    def aumentar_canais(self, qt_canais):
        self.nr_canais += qt_canais

    def diminuir_canais(self, qt_canais):
        self.nr_canais -= qt_canais

    def ligar(self):
        self.__ligada = True

    # criando metodo privado
    def __metodo_privado(self):
        print('Metodo Privado')

    def getAno(self):
        return self.__ano_lancamento

    def setAno(self, ano_lancamento):
        self.__ano_lancamento = ano_lancamento

    # usando property para definir getter e setter ja na declaracao
    ano_lancamento = property(fget=getAno, fset=setAno)

tv = Televisao(3)
# print(tv._Televisao__ligada)


# acessando o atributo privado
# isso nao deve ser feito, mas eh possivel
# tv._Televisao__ligada = True
# print(tv._Televisao__ligada)

tv.marca = "lalala"
print(tv.marca)



print(tv.getAno())