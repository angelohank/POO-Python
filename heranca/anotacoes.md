# Herança

## Conceito

como o nome sugere, objetos e classes que herdam coisas de outras classes

como um filho que herda a cor de cabelo do pai

[CLASSE MAE] (chamada tambem de super classe)<br> 
[CLASSE FILHA] [CLASSE FILHA]

- Toda classe herda de Object (é a mãe de todas as classes no python)

### Boas práticas
- proteger os atributos, deixando privados
- encapsular fazendo validações nos valores
- usar heranças para evitar repetição de código


## A super classe Object

### Como é feita essa herança direto na criação?
```
class Pessoa():
    pass
```
quando usamos o "()", por baixo dos panos está sendo passado `Object`

**Importante: é passado de forma implicita no python 3, no python 2 é preciso passar explicitamente o object**

- ou seja: para uma classe herdar de outra, deve-se passar a classe mae dentro dos parenteses <br>
exemplo:
```
class Bulldog(Cachorro): #bulldog herda de Cachorro
    pass
```


## Utilidade principal da herança

- nao repetir código

exemplo
```
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
```

note como `Gerente` tem alguns atributos iguais a `Funcionario`, e alguns a mais

o que acontece quando surgir a classe `Secretário`, que tambem tem `nome` e `salario` ?

*repetição de código*


## Usando as heranças

código antigo, antes das heranças em `exemplo_funcionarios.py`

quando uma classe herda da outra, é preciso chamar o contrutor aninhado

```
Gerente(Funcionario)
        def __init__(self, senha, qt_subordinados, nome, salario):
        Funcionario.__init__(self, nome, salario)
        self.qt_subordinados = qt_subordinados
        self.senha = senha
```

o que acontece aqui: preciso receber o nome e salario no construtor da **classe filha**, e chamar o __init__ da **classe mae**

## Método super

- elimina a necessidade de colocar exatamente a classe mae no construtor da classe filha
- elimina a necessidade de passar o self

sintaxe:
`super().__init__(argumento1, argumento2)`

## Tipo É UM

"isso é um ?" <br>
"uma secretaria é um funcionario", "um gerente é um funcionario", "bulldog é um cachorro"

para saber quem herda de quem, existem alguns métodos mágicos

- TODO colocar os metodos aqui

## Sobreescrever métodos

- situação: os funcionários de uma empresa recebem um bonus anual sobre o seu salario, porém, depende do cargo

```
gerentes recebem um bonus de 15%

secretarios recebem um bonis de 10%

```

para esses casos, usa-se a sobrecarga de métodos: para a classe gerente ele faz uma coisa (retorna 15%), e a classe de secretario faz outra (retorna 10%)