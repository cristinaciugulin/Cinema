from Film import Film


class Drama(Film):

    def __init__(self, titlu, durata, gen, varsta_minima=16):
        super().__init__(titlu, durata, gen)
        self.varsta_minima = varsta_minima

