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
#         print("Avesta este puterea calculata: ", numar)
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





