# Python orientado a objetos

- criar funções: def
  - `def nr_canais`
- criar classes: class
  - `class Televisao()` 
  - por convensão, o nome da classe **sempre** inicia com letra maiuscula
  - as classes precisam ter pelo menos um metodo, parametro, ou algo dentro dela
  - caso seja uma classe que esta sendo construída, pode-se usar o `pass`
  ```
  class Televisao():
    pass
    ```
  
<hr>

## Função construtora

sintaxe:
```
def __init__()
```

- função chamada na hora que é criada uma instância do objeto
- obrigatóriamente ela precisa de 1 argumento, que é o `self` (é apenas um nome, mas por conversão, se utiliza ele)
  - argumento que referencia o próprio objeto quando ele é criado