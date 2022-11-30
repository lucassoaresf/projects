class Programa:

    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, new_name):
        self._nome = new_name.title()

    def imprimir(self):
        print(f'{self._nome} - {self.ano} - {self._likes} Likes')

class Filmes(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def imprimir(self):
        print(f'{self._nome} - {self.ano} - {self.duracao} minutos - {self._likes} Likes')

class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def imprimir(self):
        print(f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes')


vingadores = Filmes('vingadores: ultimato', 2019, 180)
vingadores.dar_like()

b99 = Serie('b99', 2013, 8)
b99.dar_like()
b99.dar_like()


filmes_e_series = [vingadores, b99]

for programa in filmes_e_series:
    programa.imprimir()

