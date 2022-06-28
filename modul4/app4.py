# Cereți input de la utilizator cu username și parola dorită. Se cere o funcție care sa
# verifice dacă are lungimea de minim 7 caractere, conține o cifra și una din următoarele
# caractere: !,@,%.

# def ismypwd():
#     good_password = False
#     while not good_password:
#         my_input = input("Introduceti o parola: ")
#         for number in range(0, 10):
#             if str(number) in my_input:
#                 break
#         else:
#             print('Parola nu contine o cifra. ')
#             continue
#         if len(my_input) < 7:
#             print("Parola trebuie sa aiba lungimea mai mare de 7 caractere.")
#             continue
#         for letter in "!@%":
#             if letter in my_input:
#                 break
#         else:
#             print('Parola nu contine un caracter special. ')
#             continue
#         if my_input[0] == my_input[0].upper():
#             good_password = True
#         else:
#             print("Prima litera este mica. ")
#             continue
#
# ismypwd()

#Creați o aplicație care sa ceara input de la utilizator cu un număr. Creați o funcție care
# sa ia ca parametru numărul introdus de către utilizator si sa calculeze puterea acestuia.
# Cereți input de la utilizator în interiorul unei bucle infinite. Dacă utilizatorul dorește sa
# iasa, trebuie sa scrie q.


# def app():
#     numar = 5
#     while True:
#         putere = input("Introdu un numar: ")
#         if putere == "q":
#             break
#         numar = numar ** int(putere)
#
#         print("Aceasta este puterea calculata: ", numar)
#
# app()

# Într-un birou se afla 3 PC-uri. Creați un script care sa ceara admin si user pentru fiecare
# din cele 3 PC-uri si sa mapeze user-ul fiecărui PC cu parola acestuia într-un dictionar.
# Afișați credentialele în formatul următor:

# def checklogs():
#     users = []
#     passwords = []
#     for i in range(1, 4):
#         users.append(input(f"User PC{i}: "))
#         passwords.append(input(f"Password PW{i}: "))
#     for i in range(3):
#         print(f"{users[i]} --> {passwords[i]}")
# checklogs()

#cu dictionar

# def checklogs():
#     acces = {}
#     for i in range(1, 4):
#         acces[input(f"User PC{i}: ")] = input(f"Password PW{i}:")
#     for user,parola in acces.items():
#         print(f"{user} --> {parola}")
#     print(acces)
# checklogs()

#----4----

angajat1 = {
'nume': 'Ana-Maria Popescu',
'departament': 'IT',
'ID': 3409,
'Salar': 4560,
}
angajat2 = {
'nume': 'Marian Muntean',
'departament': 'IT',
'ID': 2235,
'Salar': 4556,
}
angajat3 = {
'nume': 'Maria Manea',
'departament': 'HR',
'ID': 1908,
'Salar': 6755,
}
angajat4 = {
'nume': 'Oana Popa',
'departament': 'HR',
'ID': 1977,
'Salar': 5400,
}
angajat5 = {
'nume': 'David Codru',
'departament': 'Management',
'ID': 1988,
'Salar': 12900,
}

lista_dict = [angajat1, angajat2, angajat3, angajat4, angajat5]

#a)

for angajat in lista_dict:
    if angajat['Salar'] > 5000:
        print(f"{angajat['nume']} -> {angajat['departament']}{angajat['ID']}")

#b)

list = []
for angajat in lista_dict:
    if angajat['departament'] != 'Management':
        list.append(angajat['nume'])
    print(list)

#c)

counter = 0
suma = 0
for angajat in lista_dict:
    if angajat['departament'] == 'HR':
        counter += 1
        suma += angajat['Salar']
print(suma/counter)