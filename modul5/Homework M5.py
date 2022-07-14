#1.
import random
adauga_cnp = input("CNP:")
valoare_bon = input("Introduceti valoarea bonului:")
cnp = list(map(int, adauga_cnp))
if len(cnp) == 13:
    print("CNP-ul este valid")
else:
    raise Exception("CNP invalid !")

def validare_varsta():

    current_year = 2022
    if int(adauga_cnp[1]) == 0:
        list = ["20"]
        list.append(adauga_cnp[1])
        list.append(adauga_cnp[2])
        year_of_birth = "".join(list)
        age = current_year - int(year_of_birth)
        print(age)
        if age >= 18:
            print('OK')
        else:
            raise Exception("esti minor , ia suzeta")
    else:
        list2 = ["19"]
        list2.append(adauga_cnp[1])
        list2.append(adauga_cnp[2])
        year_of_birth2 = "".join(list2)
        age = current_year - int(year_of_birth2)
        print(age)
        if age > 18:
            print('OK')
        else:
            raise Exception("esti minor , stai acasa")

validare_varsta()
lista_premii1 =["un suc", "o punga de chipsuri", "o caserola de prajituri"]
lista_premii2 =["un prajitor de paine", "o consola de gaming", "o tastatura mecanica"]
lista_premii3 =["un robot de bucatarie", "o masina", lista_premii1[0], lista_premii1[1], lista_premii1[2], lista_premii2[0], lista_premii2[1], lista_premii2[2]]


if valoare_bon == int and float:
    if int(valoare_bon) < 100:
        print("Ati castigat:", random.choice(lista_premii1), "\nFelicitari!!!!")
    if int(valoare_bon) in range(100, 500):
        print("Ati castigat:", random.choice(lista_premii2), "\nFelicitari!!!!")
    if int(valoare_bon) > 500:
        print("Ati castigat:", random.choice(lista_premii3), "\nFelicitari!!!!")
else:
    valoare_bon == str
    print("Nu ati introdus o valoare corecta.")
