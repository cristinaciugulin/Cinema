class Film:
    def __init__(self, titlu, durata, gen):
        self.titlu = titlu
        self.durata = durata
        self.gen = gen


    def durata_maxima_film(self):
        if self.durata >= 180:
            raise ValueError("Durata filmelor trebuie sa fie de cel mult 180 de minute.")
        else:
            return self.durata