#aplicatie magazin

class Product:

    def __init__(self):
        self.category = input("Introduceti numele categoriei: ")
        self.name = input("Introduceti numele produsului: ")
        self.price = input("Introduceti pretul produsului: ")
        self.stock = input("Introduceti stocul produselor:: ")

    def __repr__(self):
        return 10 * "=" + "\n" + f"Categoria: {self.category}" + "\n" +10 * "=" + "\n"


if __name__ == "__main__":
    camasi = Product()
    print(camasi)