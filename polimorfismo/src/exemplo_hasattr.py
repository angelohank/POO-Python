class Engenheiro:
    def __init__(self, nome):
        self._nome = nome

    def get_nome(self):
        return self._nome

eng = Engenheiro('angelo')
print(hasattr(eng, '_nome')) #true
print(hasattr(eng, 'nome')) #false