class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa = Pessoa("angelo", 25)
dir(pessoa) #retorna os metodos dessa minha instancia

#é possivel adicionar novos metodos direto na instancia, sem passar pela classe
pessoa.sexo = 'M'

dir(pessoa) #retorna os metodos dessa minha instancia