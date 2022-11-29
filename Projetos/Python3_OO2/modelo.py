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

class Filmes(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao


class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas


vingadores = Filmes('vingadores - ultimato', 2019, 180)
vingadores.dar_like()
print(f'{vingadores.nome} - {vingadores.ano} - {vingadores.duracao} minutos - {vingadores.likes}')

b99 = Serie('b99', 2013, 8)
b99.dar_like()
b99.dar_like()
print(f'{b99.nome} - {b99.ano} - {b99.temporadas} temporadas - {b99.likes}')
