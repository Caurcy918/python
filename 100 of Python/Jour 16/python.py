from prettytable import PrettyTable

x = PrettyTable()

x.add_column("City name",["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"])
x.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386])
x.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092, 1554769])
x.add_column("Annual Rainfall",[600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9, 869.4])
print(x)

y = PrettyTable()
y.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
y.add_column("Type",["Electric","Water","Fire"])
#print(y.align)
y.align = "l"
print(y)

# Un object in OOP is an instance of a class
# Each unique object can have attributes and methods
# An attribute is a characteristic of an object
# A method is an operation we can perform with the object
# A method is a function that is associated with an object
# A class is a blueprint for creating objects

# Exemple of a class(object) in Python
# class User:
#     pass

# user_1 = User()

# user_1.first_name = "Joe" # first_name is an attribute
# user_1.last_name = "Smith" # last_name is an attribute
# Une méthode est une fonction qui est associate à un objet
# class User:
#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"

# my_fiat = Car() : my_fiat is an object of the class Car
