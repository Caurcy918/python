import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
           "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
           "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
           "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

symbols = ["!", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">",
           "?", "@", "[",
           "]", "^", "_", "`", "{", "|", "}", "~"]

print("Welcome to the PyPassword Generator! ")
nb_letters = int(input("How many letters would you like in your password? "))
nb_symbols = int(input("How many symbols would you like in your password? "))
nb_numbers = int(input("How many numbers would you like in your password? "))

password = []

for i in range(nb_letters):
    password.append(random.choice(letters))

for i in range(nb_symbols):
    password.append(random.choice(symbols))

for i in range(nb_numbers):
    password.append(random.choice(numbers))

password = "".join(password)

print("Your password is: " + password)