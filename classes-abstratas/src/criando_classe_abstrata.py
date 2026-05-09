import abc
from abc import ABC, abstractmethod

class Animal(abc.ABC):
    def __init__(self, especie, nome):
        self.especie = especie
        self.nome = nome

    @abc.abstractmethod
    def fazer_barulho(self):
        pass

class Dog(Animal):
    def __init__(self, especie, nome):
        super().__init__(especie, nome)

    def fazer_barulho(self):
        print('auau')

dog = Dog('Dog', 'Dog')
dog.fazer_barulho()