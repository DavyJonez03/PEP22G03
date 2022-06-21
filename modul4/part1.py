# --Functii--

# def putere_doi(x):
#     print(x * x)
#     # return None # implicit
#
# def putere_n(x,n):
#     return x ** n
#
# print(putere_doi(3))
#
#
# putere_doi(3)
#
# result = putere_n(4, 5)
# print(result)
#
# print(putere_n(3, 3))

# --Argumente--

# def putere_n(n, x, add=100, sub=0):
#     print('Valoare1 argument cheie', add)
#     print('Valoare2 argument cheie', sub)
#     print('Variabilele sunt:', x, n)
#     return x ** n + add + sub
#
# putere_n(3, 4, add=201)
# putere_n(3, 4, 200)
# putere_n(3, 4, 200, 150)
# putere_n(3, 4, add=200, 150)
#print('Variabilele sunt:', x, n) - local scope only

# --Variabile--

add = 200
sub = 100
div = 3
def putere_n(n, x, add=100, sub=0):
    print('Valoare1 argument cheie', add)
    print('Valoare2 argument cheie', sub)
    print('Variabilele sunt:', x, n)
    return x ** n + add + sub

print(putere_n(3, 3))












