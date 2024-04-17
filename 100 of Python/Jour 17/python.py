class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old")


user = User("Alice", 25)

user.say_hello()


class Admin:
    pass


admin = Admin()
admin.id = 1
admin.name = "Bob"
admin.age = 30
print(f"Admin {admin.name} has id {admin.id} and is {admin.age} years old")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("Charlie", 35)
print(f"Person {person.name} is {person.age} years old")


class Number:

    def __init__(self, user_data, username):
        self.user_id = user_data
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user_1):
        user_1.followers += 1
        self.following += 1


user_2 = Number(1, "Alice")
user_3 = Number(2, "Bob")
print(f"{user_2.username} has {user_2.followers} followers and is following {user_2.following} users")
print(f"{user_3.username} has {user_3.followers} followers and is following {user_3.following} users")