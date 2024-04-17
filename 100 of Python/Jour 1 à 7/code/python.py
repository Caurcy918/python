"""name = str(len(input("What is your name?\n")))
print("Your name has been set to: " + name)

number = int(input("What is your number?\n"))
print(number - 27)

print("------------------------------------------------------")

print("Welcome to the calculator program.")
bill = float(input("What was the total bill?\n"))
tip = float(input("What percentage tip would you like to give?\n"))
number = int(input("How many people to split the bill?\n"))
print("Each person should pay: " + str(round(((bill / number)*((tip / 100) + 1)), 2)) + ".")

print("------------------------------------------------------")

year = int(input())

if year % 4 == 0 and year % 100!= 0 or year % 400 == 0:
    print("You are a leap year.")
else:
    print("You are not a leap year.")

print("------------------------------------------------------")

print("Welcome to the rollercoaster")
height = int(input("How tall are you?\n"))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("How old are you?\n"))
    if age < 12:
        bill = 5
        print("Child tickets are £5.")
    elif age < 18:
        bill = 10
        print("Youth child tickets are £10.")
    else:
        bill = 15
        print("Adult tickets are £15.")
    
    wants_photo = input("Would you like a photo taken? (y/n)\n")
    if wants_photo == "y":
        bill += 3
    print("Your total bill is £" + str(round(bill, 2)) + ".")
else:
    print("You cannot ride the rollercoaster.")
    
print("------------------------------------------------------")

print("Welcome to the rollercoaster")
height = int(input("How tall are you?\n"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("How old are you?\n"))
    
    ticket_prices = {range(0, 12): 5, range(12, 18): 10, range(18, 200): 15}
    for age_range, price in ticket_prices.items():
        if age in age_range:
            bill = price
            print(f"Your ticket price is £{price}.")
            break
    
    wants_photo = input("Would you like a photo taken? (y/n)\n")
    if wants_photo.lower() == "y":
        bill += 3
    print(f"Your total bill is £{round(bill, 2)}.")
else:
    print("You cannot ride the rollercoaster.")

print("------------------------------------------------------")

print("Thank you for choosing Python Pizza Delivery.")
size = input("What size pizza do you want? S, M, or L\n")
add_pepperoni = input("Do you want pepperoni? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")

bill = 0

if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
    
    if extra_cheese == "Y":
        bill += 1
    
    print("Your total bill is £" + str(round(bill, 2)) + ".")
elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
    
    if extra_cheese == "Y":
        bill += 1
    
    print("Your total bill is £" + str(round(bill, 2)) + ".")
elif size == "L":
    bill = 25
    if add_pepperoni == "Y":
        bill += 3
    
    if extra_cheese == "Y":
        bill += 1
        
    print("Your total bill is £" + str(round(bill, 2)) + ".")
else:
    print("Please enter a valid pizza size.")
    
print("------------------------------------------------------")

print("Thank you for choosing Python Pizza Delivery.")
size = input("What size pizza do you want? S, M, or L\n").upper()
add_pepperoni = input("Do you want pepperoni? Y or N\n").upper()
extra_cheese = input("Do you want extra cheese? Y or N\n").upper()

pizza_prices = {"S": 15, "M": 20, "L": 25}
extras = {"Pepperoni": {"S": 2, "M": 3, "L": 3}, "Extra cheese": 1}

bill = pizza_prices.get(size, 0)

if add_pepperoni == "Y":
    bill += extras["Pepperoni"].get(size, 0)

if extra_cheese == "Y":
    bill += extras["Extra cheese"]

if bill > 0:
    print(f"Your total bill is £{round(bill, 2)}.")
else:
    print("Please enter a valid pizza size.")

print("------------------------------------------------------")

print("The love Calculator is your score")
name1 = (input("What is your name?\n"))
name2 = (input("What is your name?\n"))

combined = name1 + name2
lower_combined = combined.lower()

t = lower_combined.count("t")
r = lower_combined.count("r")
u = lower_combined.count("u")
e = lower_combined.count("e")

first_letter = t + r + u + e

l = lower_combined.count("l")
o = lower_combined.count("o")
v = lower_combined.count("v")
e = lower_combined.count("e")

second_letter = l + o + v + e

score = int(str(first_letter) + str(second_letter))
if (score < 10 ) or (score > 90):
    print(f"Your score is: {score}, you go together like coke and milk")
elif (score >= 40) and (score <= 50):
    print(f"Your score is: {score}, you alright together")
else:
    print(f"Your score is: {score}")
"""

