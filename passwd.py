#encode
def encode(password):
    encoded_password = ''.join(str((int(char) + 3) % 10) for char in password)
    return encoded_password
#decode
def decode(password):
    decoded_password = ''.join(str((int(char) - 3) % 10) for char in password)
    return decoded_password

def main():
    stored_password = None
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        choice = input("Please enter an option: ")

        if choice == '1':
            password = input("Please enter the password to encode: ")
            stored_password = encode(password)
            print("Your password has been encoded and stored!")
        elif choice == '2':
            if stored_password is None:
                print("No encoded password stored. Please encode a password first.")
            else:
                decoded_password = decode(stored_password)
                print(f"The encoded password is {stored_password}, and the original password is {decoded_password}.")
        elif choice == '3':
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
