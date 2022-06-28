# lista1=["A", "B", "C"]
# print(lista1[0])
# print(lista1[1])
#
# dictionar={"fructe": ["mere", "pere"], "legume": ["rosii", "castraveti"]}
# print(dictionar ["legume"] [1])
# print(dictionar.keys())
#
# dictionary_keys = dictionar.keys()
# for key in dictionary_keys:
#         print(key)


#Using one of the comparison operators in Python, write a simple two-line
# program that takes the parameter n as input, which is an integer, and
# prints False if n is less than 100, and True if n is greater than or
# equal to 100.

# n = int(input())
# print(bool(2 * n < 100))
# print(bool(2 * n >= 100))

# print(2*n<100"\n"2*n>=100"\n")

#MODUL 3:
#PROBLEMA 1
# name = input("The plant is:")
# if name == "Spathiphyllum":
#     print("Yes - Spathiphyllum  is th best pant ever")
# elif name == "Spathiphyllum".lower():
#     print("No, I want a big Spathiphyllum!")
# else:
#     print("Spathiphyllum! Not " +name+"!")
#PROBLEMA 2
# income = float(input("Enter the annual income: "))
# tax = 0
# if income <=  85528:
#     tax = 18 / 100 * income - 556.2
# elif income > 85528:
#     tax = 14839 + 32 / 100 * (income - 85528)
#
# if tax <= 0:
#     tax = 0
#
# tax = round(tax, 0)
# print("The tax is:", tax, "thalers")

#counter 5,4,3,2,1,0
# counter = 5
# while counter:
#     print("Inside the loop.", counter)
#     counter -= 1
# print("Outside the loop.", counter)

#problema modulul 3

# secret_number = 777
# name = int(input())
# while name != secret_number:
#     print("Ha ha! You're stuck in my loop!")
# else:
#     print("Well done, muggle! You are free now.")
text = "OpenEDG Python Institute"
for letter in text:
    if letter == "P":
        break
    print(letter, end="")

