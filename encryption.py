from generateRandom import generateRandom
import os.path
import hashlib

def makeStars():
    print("\n" + "*"*10)

def readContentOfFile(pathToFile):
    if not os.path.exists(pathToFile):
        print("Please provide a valid path to your file!")
        return None
    with open(pathToFile, 'r', encoding="utf-8") as f:
        message = f.read()
    return message

def encryptMessage(message, fullKey):
    encryptedMessage = ""
    for char in message:
        encryptedMessage += chr((ord(char)+fullKey))
    return encryptedMessage
    
def decryptMessage(encryptedMessage, fullKey):
    decryptedMessage = ""
    for c in encryptedMessage:
        decryptedMessage += chr(ord(c)-fullKey)
    return decryptedMessage 

def encrypt(checkMode=True):
    message = readContentOfFile("message.txt")
    hashOfEncryptedMessage = hashlib.sha512(message.encode("utf-8")).hexdigest()  
    if checkMode:
        makeStars()
        encryptedMessage = encryptMessage(message, firstUserFullKey)
        with open("encrypted_message.txt", 'w') as file:
            file.write(encryptedMessage)
        print(f"Your message before encryption: {message}")
        print(f"SHA-512 hash of the above message: {hashOfEncryptedMessage}")
        print(f"Your encrypted message: {encryptedMessage}")
        print(f"Saving encrypted message to file encrypted_message.txt")
        makeStars()
    return hashOfEncryptedMessage
    
def decrypt(checkMode=True):
    encryptedMessage = readContentOfFile("encrypted_message.txt")
    decryptedMessage = decryptMessage(encryptedMessage, firstUserFullKey)
    hashOfDecryptedMessage = hashlib.sha512(decryptedMessage.encode("utf-8")).hexdigest()
    if checkMode:
        makeStars()
        print(f"Your message before decryption: {encryptedMessage}")
        print(f"Decripted message: {decryptedMessage}")
        print(f"SHA-512 hash of the decrypted message: {hashOfDecryptedMessage}")
        makeStars()
    return hashOfDecryptedMessage

def printInfo():
    makeStars()
    print(f"First user has {firstUserPublicKey} as a public key and {firstUserPrivateKey} as a private one")
    print(f"Second user has {secondUserPublicKey} as a public key and {secondUserPrivateKey} as a private one")
    print(f"Full key of a first user {firstUserFullKey}")
    print(f"Full key of a second user {secondUserFullKey}")
    makeStars()

def compareHashes():
    makeStars()
    if not os.path.exists("message.txt") or not os.path.exists("encrypted_message.txt"):
        print("Please encrypt and decrypt file first!")
        return

    hashOfEncryptedMessage = encrypt(False)
    hashOfDecryptedMessage = decrypt(False)

    if (hashOfEncryptedMessage == hashOfDecryptedMessage):
        print("Hashes are equal")
    else:
        print("Hashes are not equal")
    makeStars()

def addRandomStuff():
    with open("encrypted_message.txt", 'a') as file:
        file.write("RANDOM STUFF TO MESS WITH HASH")
    print("\nAdded random stuff to encrypted_message.txt\n")


def main():
    print("*"*10)
    print("Lukasz Wolynski BST 2022 - algorytm Diffie-Hellmana")
    print("*"*10)
    while(True):
        print("1. Encrypt message")
        print("2. Decrypt message")
        print("3. Check info about keys")
        print("4. Compare hashes of encrypted and decrypted message")
        print("5. Add some random stuff to change hash")
        print("6. Exit")
        print("\n")

        choice = input("What to you want to do: ")
        if choice == "1":
            encrypt()
        elif choice == "2": 
            decrypt()
        elif choice == "3":
            printInfo()
        elif choice == "4":
            compareHashes()
        elif choice == "5":
            addRandomStuff()
        else:
            exit()


# ****************************************************************
# KEYS GENERATION
# ****************************************************************
print("Generatig keys. Please wait...")
firstUserPublicKey, firstUserPrivateKey   =  generateRandom()
secondUserPublicKey, secondUserPrivateKey =  generateRandom()
firstUserPartialKey = pow(firstUserPublicKey, firstUserPrivateKey, secondUserPublicKey)
secondUserPartialKey = pow(firstUserPublicKey, secondUserPrivateKey, secondUserPublicKey)
firstUserFullKey = pow(secondUserPartialKey, firstUserPrivateKey, secondUserPublicKey)
secondUserFullKey = pow(firstUserPartialKey, secondUserPrivateKey, secondUserPublicKey)

if __name__ == "__main__":
    main()



#pip3 install scipy
