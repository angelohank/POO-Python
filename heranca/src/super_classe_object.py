class Funcionario:
    pass

# a classe nao tem nada, mas se usar o __dir__, varios metodos sao mostrados
# eles vem da super classe Object
funcionario = Funcionario()


print(dir(object))