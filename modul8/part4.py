# lambda functions

def add_numbers(a, b):
    return a + b

print(add_numbers)
print("Normal function", add_numbers(10, 20))

add_numbers_ = lambda a, b: a + b # we do not need "add_numbers_" variable here !
print(add_numbers_)
print("Lambda function", add_numbers_(10, 20))


def apply_function(a, b, c):
    return a(b, c)

print("Rezultatul calculului este:", apply_function(add_numbers, 15, 16))
print("Rezultatul calculului este:", apply_function(add_numbers_, 15, 16))
print("Rezultatul calculului lambda este:", apply_function(lambda a, b: a + b, 15, 16))

for i in range(100):
    print("Rezultatul calculului cu lambda este:", apply_function(lambda a, b: a + b + i, 15, 16))


# Map the function

map(lambda i: i + 5, [1, 2, 3, 4])
print(result)
print(list[result])
for i in result:
    print(i)

# Filter the function

