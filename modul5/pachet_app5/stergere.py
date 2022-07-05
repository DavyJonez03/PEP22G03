#Stergere produs

def stergere_func(inventar:dict):
    #from app5 import inventar
    produse = input("cate produse doriti sa stergeti?:  ").strip()
    del inventar[produse]