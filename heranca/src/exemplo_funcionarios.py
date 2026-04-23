class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

class Gerente:
    def __init__(self, nome, salario, senha, qt_subordinados):
        self.nome = nome
        self.salario = salario
        self.qt_subordinados = qt_subordinados
        self.senha = senha

    def validar(self, senha):
        if(senha == self.senha):
            print(f"Acesso permitido")
            return True

        print(f"Senha negado")
        return False

class Secretaria():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario