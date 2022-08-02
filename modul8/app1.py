'''generator for prime numbers'''

def prime_generator():
    counter = 2
    while True:
        for j in range(2, counter):
            if counter % j == 0:
                break
        else:
            yield counter
        counter += 1

prime = prime_generator()
print(next(prime))
print(next(prime))


