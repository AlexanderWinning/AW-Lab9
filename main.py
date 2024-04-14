def encode(text):
    for i in text:
        if int(i) < 7:
            i += 3
        else:
            i -= 7
    return text


if __name__ == "__main__":
    option = ""
    while option != "3":
        print("""------
        1. Encode
        2. Decode
        3. Exit
        """)
        option = input("Please enter an option: ")
        if option == "1":
            plaintext = input("Please enter your password to encode: ")
            encoded = encode(plaintext)
            print(f"{encoded} is your password encoded!")
            print("")
        elif option == "2":
            encoded = input("Please enter your password to decode: ")
            decoded = decode(encoded)
            print(f"{decoded} is your password decoded!")
            print("")
        elif option == "3":
            print("Thank you for using this program!")
        else:
            print("Invalid option, try again.")
            print("")
            