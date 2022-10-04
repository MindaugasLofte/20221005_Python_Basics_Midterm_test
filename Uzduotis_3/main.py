# Duotas "audi" žodynas.

# Parašykite funkciją "get_dict_values", kuri:
# * Turės 'docstring' tipo komentarą apie tai, ką ji atlieka.
# * Nekeis žodyno, priimto kaip argumento, savo viduje.
# * Kaip argumentą priims žodyną ir grąžins sąrašą su visomis jo reikšmėmis (values).

audi = {
  "make": 'audi',
  "model": 'A6',
  "year": 2005,
  "color": 'white',
}

def get_dict_values(input_list):
  """ funkcija išaukia metodą .values(), kuris grąžina tik žodyno Values. O construktoriaus list() pagalbą values pateikia
   kaip listą . P.s. input_list' reiškia tik  kad fukcija laukia 1 kintamojo.
  """
  print("Trečios užduoties atsakymas, kuris Kaip argumentą priims žodyną ir grąžins sąrašą su visomis jo reikšmėmis (values): ")
  return list(input_list.values())
print(get_dict_values(audi))
