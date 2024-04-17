""" 
import math

def paint_calk(height, width, cover):
    num_cans = (height * width) // cover
    round_of_cans = math.ceil(num_cans)
    print(f"The area of the calk is {round_of_cans * cover}")

test_h = int(input("Enter the height of the calk: "))
test_w = int(input("Enter the width of the calk: "))
coverage = 5
paint_calk(height=test_h, width=test_w, cover=coverage)

print("----------------------------------------------")

def prime_number(number):
    for i in range(2, number):
        if number % i == 0:
            print("It's not a prime number.")
        else:
            print("It's a prime number.")
            break

test_num = int(input("Enter a number: "))
prime_number(test_num)

print("----------------------------------------------")

def prime_number(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if number % i == 0:
            print("It's not a prime number.")
    else:
        print("It's a prime number.")

test_num = int(input("Enter a number: "))
prime_number(test_num)

print("----------------------------------------------")
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", 
            "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    cipher_text = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift
            if new_position > 25:
                new_position -= 26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter
    print(f"The encoded text is: {cipher_text}")
    
print("----------------------------------------------")

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", 
            "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f",
            "g", "h", "i", "j", "k", "l", "m", "n", "o", 
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

def decrypt(cipher_text, shift_amount):
    plain_text = ""  # create an empty string to store the plain text
    for letter in cipher_text:
        if letter in alphabet:  # if the letter is in the alphabet
            position = alphabet.index(letter)  # find the position of the letter
            new_position = position - shift_amount  # subtract the shift amount from the position
            new_letter = alphabet[new_position]  # get the new letter
            plain_text += new_letter  # add the new letter to the plain text
    print(f"The decoded text is: {plain_text}")



if direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)
elif direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
else:
    print("Invalid choice.")
"""
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", 
            "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f",
            "g", "h", "i", "j", "k", "l", "m", "n", "o", 
            "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
""" 
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

def decrypt(cipher_text, shift_amount):
    plain_text = ""  # create an empty string to store the plain text
    for letter in cipher_text:
        if letter in alphabet:  # if the letter is in the alphabet
            position = alphabet.index(letter)  # find the position of the letter
            new_position = position - shift_amount  # subtract the shift amount from the position
            new_letter = alphabet[new_position]  # get the new letter
            plain_text += new_letter  # add the new letter to the plain text
    print(f"The decoded text is: {plain_text}")



if direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)
elif direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
else:
    print("Invalid choice.")
"""

