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

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} Likes'


class Filmes(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} minutos - {self._likes} Likes'


class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes'


class Playlist(list):
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)


vingadores = Filmes('vingadores: ultimato', 2019, 180)
b99 = Serie('b99', 2013, 8)
avatar = Filmes('avatar', 2022, 180)
hotd = Serie('House of the Dragon', 2022, 1)

vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
avatar.dar_like()
avatar.dar_like()
avatar.dar_like()
avatar.dar_like()
b99.dar_like()
b99.dar_like()
hotd.dar_like()

filmes_e_series = [vingadores, b99, hotd, avatar]
fds = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho da Playlist: {len(fds.listagem)}')

for programa in fds.listagem:
    print(programa)
