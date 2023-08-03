run_again = True

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' , 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
while run_again == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    length = len(alphabet)
    if shift > 26:
        shift = round(shift%26)

    def encrypt(text , shift):
        cipher_letter = ''
        for letter in text:
            postion  = alphabet.index(letter)
            new_position = postion + shift
            new_letter = alphabet[new_position]
            cipher_letter = new_letter
            print(cipher_letter , end='')

    def decrypt(text , shift):
        cipher_letter = ''
        for letter in text:
            postion  = alphabet.index(letter)
            new_position = postion - shift
            new_letter = alphabet[new_position]
            cipher_letter = new_letter
            print(cipher_letter , end='')

    if direction == "encode":
        encrypt(text , shift)

    if direction == "decode":
        decrypt(text , shift)
      
    ask_user = input("\nDo you need to try this again :\n").lower()

    if ask_user == "no":
        run_again = False
        print("\nGood Bye!")
    else:
        run_again






