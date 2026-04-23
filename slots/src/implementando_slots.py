class Pessoa:

    _num_pessoas = 0 #IMPORTANTE: atributos de classe nao podem estar mapeado nos slots, pois sao do escopo da classe

    #definindo que nao deve existir nenhum atributo que nao esteja nessa lista
    __slots__ = ['idade', 'nome']

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        Pessoa._num_pessoas += 1

    @classmethod
    def get_num_pessoas(cls):
        return cls._num_pessoas


pessoa = Pessoa('Angelo', 5)
print(dir(pessoa))

pessoa.sexo = 'M' #quando fizer isso, retorna erro, pois Pessoa nao tem sexo mapeado nos slots
print(dir(pessoa))