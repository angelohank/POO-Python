class Pessoa():
    def __init__(self, nome):
        self._nome = nome

class Animal():
    def __init__(self, nome):
        self._nome = nome

angelo = Pessoa('angelo')
jonas = Animal('jonas')

print(isinstance(angelo, Pessoa)) #true
print(isinstance(jonas, Pessoa)) #false
print(isinstance(jonas, Animal)) #true