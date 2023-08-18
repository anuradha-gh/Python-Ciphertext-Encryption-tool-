def encrypt(Plaintext, Key):
    EnCpt = ""

    for char in Plaintext:
        if char.isalpha():
            shift = Key % 26
            if char.islower():
                EnCpt += chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                EnCpt += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            EnCpt += char
    
    return EnCpt

def decrypt(Ciphertext, Key):
    DCpt = ""

    for char in Ciphertext:
        if char.isalpha():
            shift = Key % 26
            if char.islower():
                DCpt += chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            else:
                DCpt += chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
        else:
            DCpt += char
    
    return DCpt

Need = input("What do you need (e-Encrypt/d-Decrypt): ")
Key = int(input("What is Your Key : "))

if Need.lower() == 'e':
    Plain = input("Enter Your Plain Text: ")
    Out = encrypt(Plain, Key)
    print("Encryption is:" ,Out)

elif Need.lower() == 'd':
    cipher = input("Enter Your Cipher Text: ")
    Out = decrypt(cipher, Key)
    print("Decryption is: ",Out)
