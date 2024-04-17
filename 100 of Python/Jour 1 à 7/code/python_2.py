""" 
fruits = ["apple", "banana", "cherry", "grape"]

for fruit in fruits:
    print(fruit)
    print(fruit + "\n" + "pie")

print("-------------------------------------------------------------------------------")


student_heights = input("Enter the heights of the students: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height += height
print(f"The total height of the students is {total_height}")

number_of_students = 0

for height in student_heights:
    number_of_students += 1
print(f"There are {number_of_students} students in the class.")

average_height = round(total_height / number_of_students)

print(f"The average height of the students is {average_height}")

print("-------------------------------------------------------------------------------")


student_scores = input("The scores of the students: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

highest_score = 0

for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"The highest score is {highest_score}")


total = 0
for number in range(1, 101):
    total += number
print(f"The total is {total}")

print("-------------------------------------------------------------------------------")

target = int(input("Enter the target number: "))

even_sam = 0

for n in range(1, target + 1, 2):
    even_sam += n

print(f"The sum of the even numbers from 1 to {target} is {even_sam}")

print("-------------------------------------------------------------------------------")

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
"""




