#Mesaj cryptat si decryptat:
# key = A

my_test = 'Hello Python'
key = 'A'
encrypted_text = ''
for letter in my_test:
    letter_code = ord(letter)
    encrypted_letter = chr(letter_code ^ ord(key))
    encrypted_text += encrypted_letter
print(encrypted_text)

decrypted_text = ''
for letter in encrypted_text:
    letter_code = ord(letter)
    encrypted_letter = chr(letter_code ^ ord(key))
    decrypted_text += encrypted_letter
print(decrypted_text)