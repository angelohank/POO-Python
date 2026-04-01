# queremos um metodo que possa ser chamado via classe e via instancia sem necessidade de referenciar esse objeto
class Pessoa:

    _num_pessoa = 0

    def __init__(self, idade):
        self.__idade = idade
        Pessoa._num_pessoa += 1 # precisa referenciar a classe
        self._num_pessoa +=1 # isso vai fazer com que apenas a instancia atual receba a atualização


p1 = Pessoa(5)
p2 = Pessoa(8)
print(p1._num_pessoa)