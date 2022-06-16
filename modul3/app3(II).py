#Mesaj cryptat si decryptat:
# key = A

# my_test = 'Hello Python'
# key = 'A'
# encrypted_text = ''
# for letter in my_test:
#     letter_code = ord(letter)
#     encrypted_letter = chr(letter_code ^ ord(key))
#     encrypted_text += encrypted_letter
# print(encrypted_text)
#
# decrypted_text = ''
# for letter in encrypted_text:
#     letter_code = ord(letter)
#     encrypted_letter = chr(letter_code ^ ord(key))
#     decrypted_text += encrypted_letter
# print(decrypted_text)

#--------------------------------------------------------------------------------------

# Luați ca input de la utilizator un cuvant si afisati numarul ocurentei primei litere din
# cuvant. Exemplu:
# Introduceti un cuvant (fara majuscule): rabdare
# r apare de 2 ori.

# cuvant = input("Intoduceti un cuvant(fara majuscule):")
# counter = 0
# for letter in cuvant:
#      if letter == str(cuvant[0]):
#         counter += 1
# print('r apare de:',counter , 'ori')

#---------------------------------------------------------------------------------------

# Creați o lista obiecte = [“Masa”, 5, “Scaun”, 4.5, [5,6,7],8]. Parcurgeți lista de obiecte și
# afișați tipul fiecăruia. Challenge: Afișați tipul obiectelor în felul următor:
# Tipul obiectului Masa este str


# my_list = ["Masa", 5, "Scaun", 4.5, [5,6,7],8]
# for object_ in my_list:
#     print("Tipul obiectului", object_, type(object_).__name__)

#---------------------------------------------------------------------------------------

# Pentru acest exercițiu aveți începutul codului care cere input de la utilizator cu un șir
# separat prin virgula și îl împarte într-o listă.
# Parcurgeti lista generata din input-ul utilizatorului si eliminati dublurile din ea

my_list = (input("Intoduceti lista de taskuri :"))
my_list_taskuri = my_list.split(",")
print(my_list_taskuri)
for task in my_list_taskuri.copy():
    my_list_taskuri.count(task)
    print(f"Task-ul: {task} se regaseste de:{my_list_taskuri.count(task)}")
    if my_list_taskuri.count(task) >1:
            my_list_taskuri.remove(task)
print(my_list)

