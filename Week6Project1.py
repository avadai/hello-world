def encrypt(letters, cipher):
    code = ""
    for ch in letters:
        if ch == " ":
            code = code + ch
        elif ch.isupper():
            code = code + chr((ord(ch) + cipher - 65) % 26 + 65)
        else:
            code = code + chr((ord(ch) + cipher - 97) % 26 + 97)

    return code


plainText = input("Enter the message you want to encrypt: ")
distance = int(input("Enter the distance: "))
print(encrypt(plainText, distance))