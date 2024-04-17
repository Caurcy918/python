""" 
def format_name(f_name, l_name):
    formated_l_name = l_name.title()
    formated_f_name = f_name.title()
    print(f"{formated_f_name} {formated_l_name}")
    
format_name("John", "Doe")

print("---------------------------------------------------")

def format_name(f_name, l_name):
    formated_l_name = l_name.title()
    formated_f_name = f_name.title()
    return f"{formated_f_name} {formated_l_name}"
    
print(format_name("John", "Doe"))

print("---------------------------------------------------")

def format_name(f_name, l_name):

# The  is used to start a multi-line comment in Python. This allows you to write multiple lines
# of comments without using `#` at the beginning of each line. It is often used for documenting
# functions or providing detailed explanations within the code.

    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_l_name = l_name.title()
    formated_f_name = f_name.title()
    return f"Result : {formated_f_name} {formated_l_name}"
    
print(format_name(input("Enter your first name: "), input("Enter your last name: ")))

print("---------------------------------------------------")

def is_leave(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leave(year):
        return 29
    return month_list[month - 1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

print("---------------------------------------------------")

def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
 
result = outer_function(5, 10)
print(result)

def my_function(a):
    if a < 40:
        return print("Terrible")
    if a < 80:
        return "Pass"
    else:
        return "Great"
print(my_function(25))

"""



