class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def get_bonus(self):
        return 0

class Gerente(Funcionario):
    def __init__(self,  nome, salario, senha, qt_subordinados):
        super().__init__(nome, salario)
        self.qt_subordinados = qt_subordinados
        self.senha = senha

    def get_bonus(self):
        return self.salario * 0.15

class Secretaria(Funcionario):
    def __init__(self, nome, salario, qt_gerentes):
        super().__init__(nome, salario)
        self.qt_gerentes = qt_gerentes

    def get_bonus(self):
        return self.salario * 0.10


class GestaoBonus:
    def __init__(self, total_bonificacao=0):
        self._total_bonificacao = total_bonificacao

    def registrar(self, funcionario):
        self._total_bonificacao += funcionario.get_bonus()

    @property
    def total_bonificacoes(self):
        return self._total_bonificacao


gerente = Gerente('ANGELO', 1000, '123', 2)
secretaria = Secretaria('CLAUDETE', 500, 2)

print(gerente.get_bonus()) # deve retornar 150
print(secretaria.get_bonus()) # deve retornar 50
