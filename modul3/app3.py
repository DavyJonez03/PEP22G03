CNP = input("introduceti primele 7 cifre din CNP:")
anul_nasterii = int(CNP[1:3])
print(anul_nasterii)
anul_curent = 2022
if int(CNP[0]) > 2:
    anul_nasterii = anul_nasterii+2000
else:
    anul_nasterii = anul_nasterii+1900
    #anul_nasterii+=1900
print(anul_nasterii)

if anul_curent-anul_nasterii > 18:
    print(anul_curent-anul_nasterii > 18)
    print("Aveti peste 18 ani.")
else:
    print("Aveti mai putin de 18 ani.")



