#Adaugare produs

def adaugare_func(inventar):
    # from app5 import inventar
    produse = input("cate produse doriti sa adaugati?:  ").split(",")
    inventar.update({produse[0].strip(): (produse[1], produse[2])})



