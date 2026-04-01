# Atributos e classes protegidos

class MyClass():
    def __init__(self, nome, descricao):
        self._nome = nome
        self._descricao = descricao
        self.__pvtAtributo = 'atributo privado'

    def printName(self):
        print(self._nome)



classe = MyClass('Classe de exemplo', 'uma classe de exemplo')

# classe.printName()
classe.__pvtAtributo = 'PVT'
print(classe.__pvtAtributo)
print(dir())

