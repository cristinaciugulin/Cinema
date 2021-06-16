from Film import Film

class Animatie(Film):
    def __init__(self, titlu, durata, gen, limba_dublare):
        super().__init__(titlu, durata, gen)
        self.limba_dublare = limba_dublare


    def limba_dublare_film(self):
        return self.limba_dublare
