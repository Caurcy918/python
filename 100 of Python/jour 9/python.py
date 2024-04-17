"""programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again."}
programming_dictionary["loop"] = "A piece of code that you can easily call over and over again."
print(programming_dictionary)

empty_dictionary = {}

programming_dictionary["Bug"] = "A moth in your computer"
#print(programming_dictionary)
for thing in programming_dictionary:
    print(thing)
    print(programming_dictionary[thing])

print("-----------------------------------------------")

student_scores = {"Harry": 81, "Ron": 78,
                  "Hermione": 99, 
                  "Draco": 74, 
                  "Neville": 62}

student_grades = {}
for student in student_scores:
    scores = student_scores[student]
    if scores >= 90:
        student_grades[student] = "A"
    elif scores >= 80:
        student_grades[student] = "B"
    elif scores >= 70:
        student_grades[student] = "C"
    elif scores >= 60:
        student_grades[student] = "D"
    else:
        student_grades[student] = "F"
print(student_grades)

print("---------------------------------------------------")

travel_log = [
    
    {"country": "Germany", 
     "cities_visited":["Berlin", "Munich", "Hamburg"], 
     "total_visited": 10},
    {
      "country": "France", 
      "cities_visited":["Paris","Lille", "Dijon"], 
      "total_visited": 5
    }
]

print("---------------------------------------------------")

country = input("Enter the country name: ") #Add country name
visits = input("Enter the number of cities visited: ") #Add number of cities visited
list_of_cities = eval(input("Enter the list of cities visited: ")) #Add list of cities visited

travel_log = [
    {
        "country": "France",
        "visited_cities": ["Paris", "Lille", "Dijon"],
        "visits": 5
    },
    {
        "country": "Germany",
        "visited_cities" : ["Berlin", "Munich", "Hamburg"],
        "visits": 10
    }
]

def add_city(travel_log, country, visited_cities, visits):
    new_country = {}
    new_country["country"] = country
    new_country["visited_cities"] = visited_cities
    new_country["visits"] = visits
    travel_log.append(new_country)
    print(travel_log)

add_city(travel_log, country, visits)

print("---------------------------------------------------")

country = input("Enter the country name: ") #Add country name
visits = input("Enter the number of cities visited: ") #Add number of cities visited
list_of_cities = eval(input("Enter the list of cities visited: ")) #Add list of cities visited

travel_log = [
    {
        "country": "France",
        "visited_cities": ["Paris", "Lille", "Dijon"],
        "visits": 5
    },
    {
        "country": "Germany",
        "visited_cities" : ["Berlin", "Munich", "Hamburg"],
        "visits": 10
    }
]

def add_new_country(name_country, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = name_country #Add country name
    new_country["visited_cities"] = cities_visited
    new_country["visits"] = times_visited
    travel_log.append(new_country)
    
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[0]['country']} {travel_log[0]['visits']} times.")
print(f"My favourite cities are {travel_log[0]['visited_cities']}.")

print("---------------------------------------------------")

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(["main"][2][0])
"""


