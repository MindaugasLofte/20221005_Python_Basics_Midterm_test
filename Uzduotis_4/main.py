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

    def was_expensive(self):
        if self.budget > 100000000:
            return True
        else:
            return False

    def __repr__(self):
        return f"({self.title}, {self.director}, {self.budget})"


movie_1 = Movie("Trys_paršeliai", "Jonas Jonaitis", 50000)
movie_2 = Movie("Čarlis ir šokolado fabrikas", "Tim Burton", 150000000)
movie_list = [movie_1, movie_2]
print(movie_list)

movie_dic = [movie_1.__dict__, movie_2.__dict__]
print(movie_dic)

print(movie_1.was_expensive())
print(movie_2.was_expensive())
