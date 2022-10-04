# Duotas "users" sąrašas.

# Parašykite dvi funkcijas, kurios:
# * Turės 'docstring' tipo komentarą apie tai, ką jos atlieka.
# * Nekeis sąrašo, priimto kaip argumento, savo viduje.
# * Atliks nurodytas užduotis:

# 1. funkcija "filter_all_or_nothing_people" - kaip argumentą priims "users"
# sąrašą ir duoto sąrašo atveju grąžins sąrašą vartotojų, kurie arba neturi
# naminių gyvūnų visiškai, arba turi ir šunį, ir katę.

# 2. funkcija "filter_underaged_owners" - kaip argumentą priims "users" sąrašą
# ir duoto sąrašo atveju grąžins sąrašą vartotojų, kurie dar nėra pilnamečiai,
# bet turi bent vieną naminį gyvūną.

users = [
    { 'id': '1', 'name': 'John Smith', 'age': 17, 'hasDog': True, 'hasCat': True },
    { 'id': '2', 'name': 'Ann Smith', 'age': 24, 'hasDog': True, 'hasCat': False },
    { 'id': '3', 'name': 'Tom Jones', 'age': 63, 'hasDog': True, 'hasCat': True },
    { 'id': '4', 'name': 'Rose Peterson', 'age': 20, 'hasDog': True, 'hasCat': False },
    { 'id': '5', 'name': 'Alex John', 'age': 25, 'hasDog': False, 'hasCat': False },
    { 'id': '6', 'name': 'Ronald Jones', 'age': 31, 'hasDog': False, 'hasCat': True },
    { 'id': '7', 'name': 'Elton Smith', 'age': 16, 'hasDog': True, 'hasCat': False },
    { 'id': '8', 'name': 'Simon Peterson', 'age': 32, 'hasDog': False, 'hasCat': True },
    { 'id': '9', 'name': 'Daniel Cane', 'age': 15, 'hasDog': False, 'hasCat': False },
]

users2 = [
    { 'id': '1', 'name': 'John Smith', 'age': 17, 'hasDog': True, 'hasCat': True },
    { 'id': '2', 'name': 'Ann Smith', 'age': 24, 'hasDog': True, 'hasCat': True },
    { 'id': '3', 'name': 'Tom Jones', 'age': 63, 'hasDog': True, 'hasCat': True },
    { 'id': '4', 'name': 'Rose Peterson', 'age': 20, 'hasDog': True, 'hasCat': True },
    { 'id': '5', 'name': 'Alex John', 'age': 25, 'hasDog': False, 'hasCat': False },
    { 'id': '6', 'name': 'Ronald Jones', 'age': 31, 'hasDog': True, 'hasCat': True },
    { 'id': '7', 'name': 'Elton Smith', 'age': 16, 'hasDog': True, 'hasCat': True },
    { 'id': '8', 'name': 'Simon Peterson', 'age': 32, 'hasDog': False, 'hasCat': False },
    { 'id': '9', 'name': 'Daniel Cane', 'age': 15, 'hasDog': False, 'hasCat': False },
]


# # >>>>>>>>>>>>>>>>>TRUMPAS būdas<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def filter_all_or_nothing_people(input_list):
    """
    Funkcija prašys perduoti 52 eilutėje listą su žodynais, p.s. 'input_list' reiškia tik  kad fukcija laukia 1 kintamojo.
    Kad nekeisti vartotojo paduoto sąrašo sukuriame naują kintamąjį 'new_list',  lambda funkcijos pagalba
    išfiltruosime žodynus su filter pagal uzduoties sąlygas) ir paverčiame juos į list struktūrą. Galiausiai vartotojas perdavęs listą gaus reikiamą rezultatą.
    """
    new_list=list(filter(lambda x:(x['hasDog']== x['hasCat']) or (x['hasDog']== x['hasCat']),input_list))
    print("TRUMPAS būdas: pirmos užduoties 1 dalies atsakymas, gražinu listą vartotojų, kurie arba neturi naminių gyvūnų visiškai, arba turi ir šunį, ir katę: ")
    return new_list

print(filter_all_or_nothing_people(users))
# print(users)

# # 2 variantas - trumpiausias atsakymas
def filter_underaged_owners(input_list):
    """
       Funkcijos aprašymas praktiškai identiškas aukčiau minėtoje užduotyje
       """
    naujas=list(filter(lambda x:((x['hasDog']==True or x['hasCat'])==True) and x['age']<18,input_list))
    print("TRUMPAS būdas: pirmos užduoties 2 dalies atsakymas, gražinu listą vartotojų, kurie  nėra pilnamečiai ir turi bent vieną naminį gyvūną ")
    return naujas
print(filter_underaged_owners(users))



#
# # >>>>>>ILGAS BŪDAS>>>>>>>>>> 1 užduotis  "filter_all_or_nothing_people" funkcija<<<<<<<<<<<< PRADŽIA<<<<<<<<<<<<
# '''
# PAAIŠKNIMAS:  nors ilgas sprendimo būdas ilgesnis, bet naudingas, kai yra daugiau užduočių ir filtrų.
# ESMĖ: sukuriamos trys funkcijos, kurios saveikauja ir galiausiai gaunamas reikiamas rezultatas.  '''
#
# def filter_all_or_nothing_people_filtras(dic):
#     '''
#     sukuriama pirma funkcija kuri filtruoja sąrašą elementus, pagal užduoties sąlygas,
#     kuris sudarytas iš žodynų. Negrąžina rezultato, nes filter_underaged_owners funkcijai reikės kito filtro
#     '''
# #  ilgesnis return:
#     # return (dic['hasDog'] == True and dic['hasCat'] == True) or (dic['hasDog'] == False and dic['hasCat'] == False)
# # trumpesnis return:
#     return (dic['hasDog']== dic['hasCat']) or (dic['hasDog']== dic['hasCat'])
# def return_list(list):
#     ''' antra funkcija kuri sudeda išfiltrutos žodynus į listą '''
#     filtered = [dic for dic in users if filter_all_or_nothing_people_filtras(dic)]
#     return filtered
# def filter_all_or_nothing_people(list):
#     ''' trečia funkcija kuri atspausdina sarašą'''
#     print("ILGAS būdas. Pirmos užduoties 1 dalies atsakymas, gražinu listą vartotojų, kurie arba neturi naminių gyvūnų visiškai, arba turi ir šunį, ir katę: ")
#     return print(f"{return_list(list)}")
# filter_all_or_nothing_people(users)
#
# # >>>>>>>>ILGAS BŪDAS>>>>>>>> 1 užduotis  "filter_all_or_nothing_people" funkcija<<<<<<<<<<<< PABAIGA<<<<<<<<<<<<
#
#
# # >>>>>>>>ILGAS BŪDAS>>>>>>>> 2 užduotis  "filter_underaged_owners" funkcija<<<<<<<<<<<< PABAIGA<<<<<<<<<<<<
# ''' 1 variantas.
# PAAIŠKNIMAS:  nors šis sprendimo būdas ilgesnis, bet naudingas, panaudosime pirmos funkcijos funkcijas, pakeisime tik filtro funkcija kai yra daugiau užduočių ir filtrų.
# ESMĖ: sukuriamos trys funkcijos, kurios saveikauja ir galiausiai gaunamas reikiamas rezultatas.  '''
#
# def filter_underaged_owners_filtras(dic):
#     '''
#     sukuriama pirma funkcija kuri filtruoja sąrašą elementus, pagal užduoties sąlygas,
#     kuris sudarytas iš žodynų. Negrąžina rezultato
#     '''
# # trumpesnis return:
#     return dic['age']<18 and (dic['hasDog']==True or dic['hasCat']==True)
# def return_list(list):
#     ''' antra funkcija kuri sudeda išfiltrutos žodynus į listą '''
#     filtered = [dic for dic in users if filter_underaged_owners_filtras(dic)]
#     return filtered
# def filter_underaged_owners(list):
#     ''' trečia funkcija kuri atspausdina sarašą'''
#     print("ILGAS būdas. Pirmos užduoties 2 dalies atsakymas, gražinu listą vartotojų, kurie  nėra pilnamečiai ir turi bent vieną naminį gyvūną ")
#     return print(f" {return_list(list)}")
# filter_underaged_owners(users)
#
# # >>>>>>>>>ILGAS BŪDAS>>>>>>> 2 užduotis  "filter_underaged_owners" funkcija<<<<<<<<<<<< PABAIGA<<<<<<<<<<<<

