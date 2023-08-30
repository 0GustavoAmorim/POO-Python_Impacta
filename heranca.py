class Mae:
    def __init__(self, p1):
        print('Executando o init de Mae')
        self.p1 = p1


class Filha(Mae):
    def __init__(self, p1, p2):
        print('Executando o init de Filha')
        super().__init__(p1)
        self.p2 = p2


class Neta(Filha):
    def __init__(self, p1, p2, p3):
        print('Executando o init de Neta')
        super().__init__(p1, p2)
        self.p3 = p3
