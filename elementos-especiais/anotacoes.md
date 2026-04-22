# Elementos especiais

## Metodos e classes estaticas
- metodos de classe: @classmethod
    - precisa do `cls` como primeiro argumento
    - cls é uma convenção da comunidade de desenvolvedores python, assim como o `self`

- metodos estaticos: @staticmethod
  - nao precisa de nenhum argumento

nenhum dos dois tipos esta ligado às instancias, e sim ao escopo da classe

## Diferença nos tipos de métodos
- @classmethod
  - entra na herança
- @staticmethod
  - não entra na herança