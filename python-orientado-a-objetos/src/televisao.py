class Televisao():
    def __init__(self, nr_canais):
        self.nr_canais = nr_canais

    def aumentar_canais(self, qt_canais):
        self.nr_canais += qt_canais

    def diminuir_canais(self, qt_canais):
        self.nr_canais -= qt_canais