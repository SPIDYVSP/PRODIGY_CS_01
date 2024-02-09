def encryption():
    print("Encryption")

    print("Message can only be Lower or Uppercase alphabet")
    msg = input("Enter message: ")
    key = int(input("Enter key(0-25): "))  

    encrypted_text = ""

    for v in range(len(msg)):
        if ord(msg[v]) == 32:  
            encrypted_text += chr(ord(msg[v]))  

        elif ord(msg[v]) + key > 122:
            temp = (ord(msg[v]) + key) - 122 
            encrypted_text += chr(96+temp)

        elif (ord(msg[v]) + key > 90) and (ord(msg[v]) <= 96):  
            temp = (ord(msg[v]) + key) - 90
            encrypted_text += chr(64+temp)

        else:
            encrypted_text += chr(ord(msg[v]) + key)

    print("Encrypted: " + encrypted_text)


def decryption():
    print("Decryption")

    print("Message can only be Lower or Uppercase alphabet")
    encrp_msg = input("Enter encrypted Text: ")
    decrp_key = int(input("Enter key(0-25): "))

    decrypted_text = ""

    for v in range(len(encrp_msg)):
        if ord(encrp_msg[v]) == 32:
            decrypted_text += chr(ord(encrp_msg[v]))

        elif ((ord(encrp_msg[v]) - decrp_key) < 97) and ((ord(encrp_msg[v]) - decrp_key) > 90):
            temp = (ord(encrp_msg[v]) - decrp_key) + 26
            decrypted_text += chr(temp)

        elif (ord(encrp_msg[v]) - decrp_key) < 65:
            temp = (ord(encrp_msg[v]) - decrp_key) + 26
            decrypted_text += chr(temp)

        else:
            decrypted_text += chr(ord(encrp_msg[v]) - decrp_key)

    print("Decrypted Text: " + decrypted_text)


def main():
    choice = int(input("1. For Encryption \n2.For Decryption \nChoose(1,2): "))
    if choice == 1:
        encryption()
    elif choice == 2:
        decryption()
    else:
        print("Wrong Choice !!")

if __name__ == "__main__":
    main()