# Duotas "users" sąrašas.

# Parašykite dvi funkcijas, kurios:
# * Turės 'docstring' tipo komentarą apie tai, ką jos atlieka.
# * Nekeis sąrašo, priimto kaip argumento, savo viduje.
# * Atliks nurodytas užduotis:

# 1. funkcija "get_user_average_age" - kaip argumentą priims "users" sąrašą ir
# duoto sąrašo atveju grąžins visų vartotojų amžiaus vidurkį kaip skaičių,
# suapvalintą iki artimiausio sveikojo skaičiaus.

# 2. funkcija "get_users_names" - kaip argumentą priims sąrašą ir duoto sąrašo
# atveju grąžins sąrašą su visų vartotojų vardais, išrikiuotais abėcėlės tvarka,
# pvz. ['Alex John', 'Ann Smith', ...].

users = [
    {'id': '1', 'name': 'John Smith', 'age': 20},
    {'id': '2', 'name': 'Ann Smith', 'age': 24},
    {'id': '3', 'name': 'Tom Jones', 'age': 31},
    {'id': '4', 'name': 'Rose Peterson', 'age': 17},
    {'id': '5', 'name': 'Alex John', 'age': 25},
    {'id': '6', 'name': 'Ronald Jones', 'age': 63},
    {'id': '7', 'name': 'Elton Smith', 'age': 16},
    {'id': '8', 'name': 'Simon Peterson', 'age': 30},
    {'id': '9', 'name': 'Daniel Cane', 'age': 51},
]


# # >>>>>>>>>>>>>>>>>Antros užduoties 1 dalis<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

def get_user_average_age(input_list):
    """
    1. funkcija "get_user_average_age" - kaip argumentą priims "users" sąrašą ir
    duoto sąrašo atveju grąžins visų vartotojų amžiaus vidurkį kaip skaičių,
    suapvalintą iki artimiausio sveikojo skaičiaus.
  """
    suma = 0
    for user in (sorted(users, key=lambda i: i['age'])):
        suma += user["age"]
    global age_average
    age_average = round(suma / len(users))
    print(
        "\nAntros užduoties 1 dalies atsakymas, grąžins visų vartotojų amžiaus vidurkį kaip skaičių, suapvalintą iki "
        "artimiausio sveikojo skaičiaus: ")
    return age_average


print(
    f"  - suapvalinta vidurkio reikšmė iki sveiko skaičiaus yra: {get_user_average_age(users)} "
    f"\n  - duomenų tipas yra: {type(age_average)}")


# # >>>>>>>>>>>>>>>>>Antros užduoties 2 dalis<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def get_users_names(input_list):
    """
    2. funkcija "get_users_names" - kaip argumentą priims sąrašą ir duoto sąrašo
    atveju grąžins sąrašą su visų vartotojų vardais, išrikiuotais abėcėlės tvarka,
    pvz. ['Alex John', 'Ann Smith', ...].
    """
    list_of_names = []
    for user in (sorted(users, key=lambda i: i['name'])):
        list_of_names.append(user["name"])
    print(
        "\nAntros užduoties 2 dalies atsakymas, kuris grąžins sąrašą su visų vartotojų vardais, "
        "išrikiuotais abėcėlės tvarka: ")
    return list_of_names


print(get_users_names(users))











# papildomi skaičiavimai ir/arba komentarai"

# pirma
"""
 Funkcija kuri lauks perduodamo vieno argumento, t.y. listo su žodynais. Jį prašys perduoti 52 eilutėje , p.s. 'input_list'
 reiškia tik  kad fukcija laukia 1 kintamojo. For ciklo pagalba loopinsime per sąrašą, kuris bus sudarytas tik iš "age" Value (tai padės
 atlikti sorted) ir kiekviena reikšmę (age value) sumuosime prie naujai sukurtos suma kintomojo reikšmės. Patogumo dėliai sukuriame
 dar vieną kitnamąjį,age_average, jį padalinus iš len (len gražina saraso ilgi) pagalba gausime vidurkį, o round
 suapvalins iki artimiausio sveiko skaičiaus.
 P.s. kintamajam global suteike savybe  būti pasiektam už funkcijos ribų.
 """
# antra
"""
  Funkcija kuri lauks perduodamo vieno argumento, t.y. listo su žodynais. p.s. 'input_list' reiškia tik  kad fukcija laukia 1 kintamojo.
  Kad nekeisti vartotojo paduoto sąrašo sukuriame naują List kintamąjį 'list_of_names'. For ciklo pagalba
  eisime per sarašą, kurį mums išfiltruos tik su names value lambda funkcija, o sorted išrikiuos pagal abecelę. Kiekvienu žingsniu
  abeceles tvarka prie list_of_names pabaigos append metodo pagalba bus pridedamas kiekviena name VALUE  į listą .
  """
