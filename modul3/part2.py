# hello = "Hello x Python"

# for letter in hello:
#     if 'x' == letter:
#         break
#     print(letter)
# else:
#     print('x is not present')


# for letter in hello:
#     if 'x' == letter:
#         continue
#     print(letter)
# else:
#     print('x was removed from string')

# my_number = 123
#
# for number in my_number:
#     if 1 == letter:
#         continue
#     print(letter)
# else:
#     print('1 was removed from number')

#how does for work:
# hello = "abc"
# iterated_object = hello.__iter__()
# print(iterated_object)
# print(next(iterated_object))
# print(next(iterated_object))
# print(next(iterated_object))
# print(next(iterated_object))_# <- end of loop (StopIteration)

# hello = range(1, 12, 2)
# print(dir(hello))
# iterated_object = hello.__iter__()
# print(iterated_object)
# print(next(iterated_object))
# print(next(iterated_object))
# print(next(iterated_object))
# print(next(iterated_object))
# print(next(iterated_object))
# print(next(iterated_object))

# Operatii pe biti
# ---Object type int---
#-4 in bits = 11111100
#-3 in bits = 11111101
#-2 in bits = 11111110
#-1 in bits = 11111111
# 0 in bits = 00000000
# 1 in bits = 00000001
# 2 in bits = 00000010
# 3 in bits = 00000011

# And bits

# print(1 and 2)
# print(1 & 2)# 00000001 &
#             00000010
#      result 00000000 = 0

# Or bits
# print(-2 or 2)
# print(-2 | 2)#11111110 |
#             00000010
#      result 11111110 = -2

#xor bits
# print(-3 ^ 3)#11111101 ^
#             00000011
#      result 11111110 = -2
# print(-2 ^ 3)#11111110 ^
#             00000011
#      result 11111101 = -3
print((146 ^ 21) ^ 21)










