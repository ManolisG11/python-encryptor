#Functions
def decryptor(phrase):
    decrypted_phrase = ""
    for letter in phrase:
        n = ord(letter)
        n2 = n - key
        decrypted_c = chr(n2)
        decrypted_phrase = decrypted_phrase + decrypted_c
    return decrypted_phrase

#Variables
key = 555

#Main
password = input("Type the password to start decrypting:")
if password == "key555":
    user_word = input("Type an encrypted phrase/word to decrypt it:")
    decrypted_word = decryptor(user_word)
    print(decrypted_word)
