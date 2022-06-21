#1.a)

# lista = ['abc', 123, '1', 1]
# for element in lista:
#     print(type(element))

#1.b)

# counter1 = 0
# counter2 = 0
# counter3 = 0
#
# for element2 in lista:
#     if type(element2) is int:
#         counter1 += 1
#     if type(element2) is float:
#         counter2 += 1
#     if type(element2) is str:
#         counter3 += 1
# print("Numarul numerelor intregi este:", counter1)
# print("Numarul numerelor reale este:", counter2)
# print("Numarul sirurilor din lista este:", counter3)

#SAU 1.b)

# integers = []
# floats = []
# strings = []
# for element in lista:
#      if type(element) is int:
#          integers.append(element)
#      if type(element) is float:
#          floats.append(element)
#      if type(element) is str:
#          strings.append(element)
#
# print("Numarul numerelor intregi este:", len(integers))
# print("Numarul numerelor reale este:", len(floats))
# print("Numarul sirurilor din lista este:", len(strings))

#2.

# lista = (input("SIR:"))
# lista = list(lista)
# lista_vocale = ['a','e','i','o','u']
# counter = 0
# for litera in lista:
#     if (litera.lower() in lista_vocale):
#         counter += 1
# print(counter)

#SAU 2.

# nume = input("Adaugati un nume:")
# lista_nume = list(nume)
# vocale = []
# for vocala in lista_nume:
#     if vocala.lower() in ('a', 'e', 'i', 'o', 'u'):
#         vocale.append(vocala)
# print("Vocale in cuvantul dvs:", len(vocale))




