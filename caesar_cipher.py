def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                new_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            elif char.isupper():
                new_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    while True:
        print("CAESAR CIPHER PROGRAM") 
        print("----------------------")
        print("1. ENCRYPTION")
        print("2. DECRYPTION")
        print("3. EXIT")
        choice = input("CHOOSE AN OPTION : ")

        print("-----------------------")

        if choice == '1':
            message = input("ENTER THE MESSAGE TO ENCRYPT : ")
            shift = int(input("ENTER THE SHIFT VALUE : "))
            encrypted_message = encrypt(message, shift)
            print(f"ENCRYPTED MESSAGE : {encrypted_message}")
        elif choice == '2':
            message = input("ENTER THE MESSAGE TO DECRYPT : ")
            shift = int(input("ENTER THE SHIFT VALUE : "))
            decrypted_message = decrypt(message, shift)
            print(f"DECRYPTED MESSAGE : {decrypted_message}")
        elif choice == '3':
            print("EXITING PROGRAM......")
            break
        else:
            print("INVALID CHOICE. PLEASE SELECT  1, 2, or 3.")

if __name__ == "__main__":
    main()
