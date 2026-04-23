class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

class Gerente(Funcionario): #agora o gerente É um FUNCIONARIO
    def __init__(self, senha, qt_subordinados, nome, salario): #esse construtor é referente à classe Gerente, apenas ela
        super().__init__(nome, salario)
        self.qt_subordinados = qt_subordinados
        self.senha = senha

    def validar(self, senha):
        if(senha == self.senha):
            print(f"Acesso permitido")
            return True

        print(f"Senha negado")
        return False
