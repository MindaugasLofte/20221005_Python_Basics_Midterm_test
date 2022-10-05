# Sukurkite filmų klasę "Movie", kuri:
# * Turės klasės lygio 'docstring' tipo komentarą, trumpai aprašantį, kas tai
#   per klasė.
# * Turės 'docstring' tipo komentarą prie kiekvieno metodo, trumpai aprašantį,
#   ką tas metodas atlieka.
# * Gebės sukurti objektus su 3 savybėmis ir 1 metodu.

# Naudojant šią klasę sukurkite bent du skirtingus filmų objektus.

# Savybės:
# * title (str)
# * director (str)
# * budget (int)

# Metodas:
# * was_expensive() - jeigu filmo "budget" yra daugiau nei 100 mln. USD,
#   grąžins True, kitu atveju - False.
class Movie:
    def __init__(self, title, director, budget):
        self.title = str(title)
        self.director = str(director)
        self.budget = int(budget)

    """sukuriame klasę Movie, kuri iš savęs duomenų nesaugo, o yra kaip instrukcija pagal kurią sukuriamas objektas 
    su savybėmis ir metodais. Movie klasė turi ne tik užduotyje minimas tris savybes, bet ir pati svarbiauia self 
    (pavadinimas gali būti kitoks, bet pagal susitarima naudojame self) savybę, ji reikalinga kiekviename metode, nes
     kai jį iškviečiame reikia žinoti su kuriuo objekto atributu turetų atlikti operacija. Kiekvienai savybei nusakeme, 
     koks duomenu tipas turi buti ivestas kuriant objekta, kitaip objektas nebus sukurtas. 
     init metodas (konstruktorius) objekta kuriant ivykdomas automatiskai. todel mes jame priskiriame kad self.title, 
     tai ka ives vartotojas ir bus title ir t.t.
      """

    def was_expensive(self):
        """ sukuriamas metodas su self savybe, galime naudoti paprasta if funkcija, arba dar paprasciau"""

        return self.budget > 100000000

    def __repr__(self):
        """ šis metodas nors ir nebuvo aprašytas užduotyje kaip būtinas, tačiau visada verta jį pasirašti, kad
        iškvietus sukurtą objektą gautumę rezultatą, kuris žmogaus akiai yra lengvai skaitomas """
        return f"({self.title}, {self.director}, {self.budget})"


# sukūrėme du objektus
movie_1 = Movie("Trys_paršeliai", "Jonas Jonaitis", 50000)
movie_2 = Movie("Čarlis ir šokolado fabrikas", "Tim Burton", 150000000)

# galime objektų reikšmes ideti i lista, bet bus idetos tik tos savybes, kurios aprasytos __repr__(self)
movie_list = [movie_1, movie_2]
print(
    f"1) Galime atspausdinti kintamaji movie_list (iš sukurtų objektų) kuriame matysime tik Values (konkrecias Values "
    f"nusakeme 36 eiluteje su repr konkstruktorium ):\n {movie_list}\n")

# #galime objektus sudeti kaip zodynus i lista,  __repr__(self) nebeturi itakos
movie_dic = [movie_1.__dict__, movie_2.__dict__]
print(f"2) Galime sukurtus objektus pridėti į listą, kaip pilnus objektus(žodynai) su keys ir values: \n{movie_dic}\n")

# dar keli papildomi atsakymai, kurie parodo, kad galima neribotai programuoti:)
print(
    f"3) Ar sukurtas objektas movie_1 kurio pavadinimas \"{movie_1.__dict__['title']}\" uždirbo daugiau nei 100mln? Atsakymas: {movie_1.was_expensive()}\n")
print(
    f"4) Ar sukurtas objektas movie_2 kurio pavadinimas \"{movie_2.__dict__['title']}\" uždirbo daugiau nei 100mln? Atsakymas: {movie_2.was_expensive()}")
