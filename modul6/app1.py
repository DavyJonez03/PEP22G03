#generic problems

"""

Create application that will ask the user for python input and format the input prompt as needed.

"""
# var1 = ">>>"
# var2 = "..."
# var3 = "    "
# counter = 0
# in_try = False
# while True:
#     x = input(f"{var1}")
#     try:
#         if x[-1] == ":":
#             counter += 1
#             var1 = "..." + counter * var3
#         if x.endswith("try:"):
#             in_try = True
#
#         if x.endswith("finally:"):
#             in_try = False
#     except IndexError:
#         if counter == 0 and not in_try:
#             quit()
#         counter -= 1
#         var1 = "..." + counter * var3


"""

Create list of prime number up to specified limit using dedicated function

"""


import random

def generate_primes(limit: int):
    result=[]
    for i in range(1, limit + 1):
        for j in range(2, i//2+2):
            if i % j == 0:
                break
        else:
            result.append(i)
    print(result)

generate_primes(100)
"""

Select 2(distinct) random numbers from prime numbers generated above.

"""

def select_primes(in_list: list):
    i = random.choice(in_list)
    in_list.remove(i[0])
    j = random.choice(in_list)
    return i[0], j[0]

print(select_primes(generate_primes(100)))



