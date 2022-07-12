def encryption_func(string,shift):

    encrypted_string = ''

    for letter in string:

        if letter == ' ':

            encrypted_string += letter

        elif letter.islower():

            #formula: c = (x + n) % 26

            encrypted_string += chr((ord(letter) + shift - 97) % 26 + 97)

        else:

            encrypted_string += chr((ord(letter) + shift - 65) % 26 + 65)

    print("Encryption successful! \nString: {}".format(encrypted_string))


def decryption_func(string,shift):

    decrypted_string = ''

    for letter in string:

        if letter == ' ':

            decrypted_string += letter

        elif letter.islower():

            #formula: c = (x + n) % 26

            decrypted_string += chr((ord(letter) - shift - 97) % 26 + 97)

        else:

            decrypted_string += chr((ord(letter) - shift - 65) % 26 + 65)

    print("Decryption successful! \nString: {}".format(decrypted_string))



if __name__ == '__main__':

    print("Caesar Cipher Function:")

    choice = input("Encrypt or Decrypt: ").lower()

    if choice[0] == 'e':

        string = input("Enter the string you want to encrypt: ")

        shift = int(input("Enter the shift to encrypt: "))

        encryption_func(string,shift)

    elif choice[0] == 'd':

        string = input("Enter the string you want to decrypt: ")

        shift = int(input("Enter the shift to decrypt: "))

        decryption_func(string,shift)