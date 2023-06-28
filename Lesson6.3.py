#Functions
def encryptor(phrase):
    encrypted_phrase = ""
    for letter in phrase:
        n = ord(letter)
        n2 = n + key
        encrypted_c = chr(n2)
        encrypted_phrase = encrypted_phrase + encrypted_c
    return encrypted_phrase

#Variables
key = 555

#Main
user_word = input("Type something to encrypt: ")

encrypted_word = encryptor(user_word)
print(encrypted_word)


##unencrypted = input("Give me a letter:")
##
##unencrypted = ord(unencrypted)
##
##encrypted = unencrypted + key
##
##encrypted = chr(encrypted)
##print(encrypted)
