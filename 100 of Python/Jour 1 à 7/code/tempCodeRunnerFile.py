alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", 
            "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    
    cipher_text = ""  # create an empty string to store the cipher text
    for letter in plain_text:
        if letter in alphabet:  # if the letter is in the alphabet
            position = alphabet.index(letter)  # find the position of the letter
            new_position = position + shift_amount  # add the shift amount to the position
            new_letter = alphabet[new_position]  # get the new letter
            cipher_text += new_letter  # add the new letter to the cipher text
    print(f"The encoded text is: {cipher_text}")


encrypt(plain_text=text, shift_amount=shift)