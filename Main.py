from Film import Film
from Drama import Drama
from Animatie import Animatie
from Cinematograf import Cinematograf
import random

if __name__ == "__main__":
    print()
    print("***************************")
    print("Bine ai venit la cinema CC!")
    print("***************************")
    print()

    cinema = Cinematograf()

    while True:
        line = input("Introduceti comanda de la tastatura: ")
        cmd = line.split()
        if cmd[0] == "adauga_drama":
            detalii_drama = input("Introduceti titlul, durata si varsta minima pentru drama (delimitate de virgula): ")
            comanda_d = detalii_drama.split(',')
            if int(comanda_d[1]) > 180:
                raise ValueError("Durata filmelor trebuie sa fie de cel mult 180 de minute.")
            else:
                cinema.lista_filme.append(Drama(comanda_d[0],comanda_d[1], "drama",comanda_d[2]))
            print(f"S-a adaugat in lista de filme: {comanda_d[0]}")
            print()
        elif cmd[0] == "adauga_animatie":
            detalii_animatie = input("Introduceti titlul,durata si limba dublare pentru animatie(delimitate de virgula): ")
            comanda_a = detalii_animatie.split(',')
            if int(comanda_a[1]) > 180:
                raise ValueError("Durata filmelor trebuie sa fie de cel mult 180 de minute.")
            else:
                cinema.lista_filme.append(Animatie(comanda_a[0], comanda_a[1], "animatie", comanda_a[2]))
            print(f"S-a adaugat in lista de filme: {comanda_a[0]}")
            print()
        elif cmd[0] == "afisare":
            print()
            print("Filmele disponibile in cinematograf sunt: ")
            for pelicula in cinema.lista_filme:
                print(f"Titlu: {pelicula.titlu}, Durata:  {pelicula.durata}, Genul: {pelicula.gen} ")
        elif cmd[0] == "afisare_animatii":
            print()
            print("Animatiile disponibile in cinematograf sunt: ")
            for pelicula in cinema.lista_filme:
                if pelicula.gen == "animatie":
                    print(pelicula.titlu)
        elif cmd[0] == "alege_film":
            film_ales = random.choice(cinema.lista_filme)
            print(f"Titlul filmului ales este: {film_ales.titlu}")
            print(f"Durata filmului ales este: {film_ales.durata}")
            print(f"Genul filmului ales este: {film_ales.gen}")

        elif cmd[0] == "salveaza_filme":
            nume_fisier = input("Introduceti numele dorit pentru fisier: (cu extensia .txt) ")
            comanda_f = nume_fisier.split()
            fisier_filme = open(comanda_f[0], "w")
            for pelicula in cinema.lista_filme:
                fisier_filme.write(pelicula.titlu + "\n")
            fisier_filme.close()
        elif cmd[0] == "exit":
            print("Aplicatia se inchide")
            exit(0)
        else:
            print("Comanda nu este recunoscuta. Incearca din nou.")