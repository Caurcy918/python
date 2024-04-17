import random
""" 
random_number = random.randint(1, 10)
print(random_number)

random_float = random.random()*10
print(random_float)

random_float_1 = random.randint(0,1)

if random_float_1 == 1:
    print("Heads")
elif random_float_1 == 0:
    print("Tails")
else:
    print("Error")

print("-------------------------------------------------------------------------------")
state_list = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Florida",
              "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana",
              "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana",
              "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina",
              "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
              "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia",
              "Wisconsin", "Wyoming"]

state_list.append("N/A")
state_list.extend(["Hope", "Market"])
for state in state_list:
    print(state)

print("-------------------------------------------------------------------------------")

names_strings = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
num_items = len(names_strings)
random_choice = random.randint(0, num_items - 1)
person_name = names_strings[random_choice]
print("You have chosen " + person_name + " as your partner.")


print("-------------------------------------------------------------------------------")

list1 = [" ", " ", " "]
list2 = [" ", " ", " "]
list3 = [" ", " ", " "]

map = [list1, list2, list3]
print("Hiding your treasure ! X marks the sports of the treasure.")
position = input("Enter the position of the treasure: ")
letter = position[0].lower()

abc = ["a", "b", "c"]
letter_position = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_position] = "X"
print(f"{list1}\n{list2}\n{list3}")
"""
def myfunction():
    print("Hello")
    print("Bye")

myfunction()

