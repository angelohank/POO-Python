# Herança múltipla

## Conceito

- uma classe que herda de mais de uma classe base (como se tivesse um pai e uma mae)

#### Problema:
- duas superclasses podem ter o mesmo metodo ou atributo
- qual deve ser usado entao?

## Problema do diamante
- ocorre quando temos herança múltipla
- chama-se "diamante" porque:

```
Classe A (base)

Classe B (herda de A)
Classe C (herda de A)

Classe D (herda de B e C) //aqui está a quarta ponta do diamante, que fecha o problema
```

se existirem métodos iguais, em qualquer das classes, A, B ou C, pode acabar sendo difícil de encontrar o método correto

- qual a ordem de prioridade usada para chamar métodos que tem o mesmo nome, mas que pertencem a classes diferentes?

resposta: em um cenário em que a classe D nao implemente o método do mesmo nome que as suas classes "pais",
o python prioriza a execucao do método que está na primeira classe passada como herança

```
class D(B, C):
    # aqui, se B e C tiverem um nome igual, usará o da classe B
```
se fosse o contrário:

```
class D(C, b):
    # aqui, se B e C tiverem um nome igual, usará o da classe C
```

## MRO - Method Resolution Order

a ordem de "procura" dos métodos pode ser verificado atraves do MRO, que é um método especial do python para classes

no caso da seguinte classe:
```
class D(B, C):
    pass

```

e eu chamar o método `__mro__`, a saida sera:
```
(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
```