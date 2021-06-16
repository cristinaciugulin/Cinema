from Film import Film
from Drama import Drama
from Animatie import Animatie


class Cinematograf:

    film1 = Drama("Schindler's List", 180, "drama")
    film2 = Drama("The Godfather", 175, "drama")
    film3 = Drama("La vita e bella", 122, "drama")
    film4 = Film("Seven Samurai", 115, "actiune")
    film5 = Drama("The Shawshank Redemption", 142, "drama")
    film6 = Drama("Titanic", 178, "drama")
    film7 = Film("Fight Club", 139, "actiune")
    film8 = Animatie("Ratatouille", 111, "animatie", "romana")
    film8 = Drama("Yes Man", 119, "drama")

    lista_filme=[film1,film2,film3,film4,film5,film6,film7, film8]