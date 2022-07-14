#generic problems

"""

Create application that will ask the user for python input and format the input prompt as needed.

"""



# var1 = ">>>"
# var2 = "...     "
#
# while True:
#     imp = input(f"{var1} ")
#     if imp == "try:":
#         imp2 = input(f"{var2}")
#         print(imp2)
#     else:
#         exit()


var1 = ">>>"
var2 = "..."
var3 = "    "
counter = 0
in_try = False
while True:
    x = input(f"{var1}")
    try:
        if x[-1] == ":":
            counter += 1
            var1 = "..." + counter * var3
        if x.endswith("try:"):
            in_try = True

        if x.endswith("finally:"):
            in_try = False
    except IndexError:
        if counter == 0 and not in_try:
            quit()
        counter -= 1
        var1 = "..." + counter * var3




